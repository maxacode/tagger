
"""
v1.1

    - Creates a controller instance with init
    - chagne brightess
    - default brighess from color-brightness table


    Usage:
    from espNeoPixelClass import setNeo, r,g,b,w
    setNeo(color) # only requires color, level(global default 0-100), pixel id(0), and reset (True) have defaults
    setNeo('green')
    setNeo(w,15,reset = False) # makes a white/green mix


"""


from neopixel import NeoPixel
from machine import Pin
from time import sleep

numOfPixels = 5
pinNumber = 48
defaultBrightness = 10

# Define RGB colors
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
off = (0, 0, 0)

# Short color codes
b = "blue"
g = "green"
r = "red"
w = "white"

# Global dictionary to store brightness levels for each color
color_brightness = {
    "red": 10,
    "green": 10,
    "blue": 10,
    "white": 15,
}

class NeoPixelController:
    def __init__(self, brightness_level: int = defaultBrightness, num_pixels: int = numOfPixels, pin: int = pinNumber) -> None:
        """Initialize the NeoPixelController with default brightness and configuration."""
        self.strip = NeoPixel(Pin(pin), num_pixels)
        self.default_brightness = brightness_level

    def apply_brightness(self, color, level):
        """Adjust color brightness by scaling RGB values."""
        scale = level / 100
        return tuple(int(c * scale) for c in color)
    
    def blend_colors(self, color1, color2):
        """Blend two RGB colors by averaging their values."""
        return tuple((c1 + c2) // 2 for c1, c2 in zip(color1, color2))
    
    def setNeo(self, color, level=None, pixel_id=0, reset=True) -> tuple(tuple(int),int) :
        """
        Set a NeoPixel to a specific color and brightness level.

        Params:
            color: required : 'red', or r (if imported)
            level: optional, defaults to defaultBrighness Global varriable or color_brightness map
            pixel_id: optional, defaults to 0
            reset: optional, defautls to True which clears the prior color, of set to False the colors get merged.
            
        Returns:
            tuple: color_with_brightness, pixel_id. ((19, 31, 19), 0)


        
        """
        if reset:
            self.strip.fill(off)
        
        # Handle color input (name or tuple)
        if isinstance(color, str):
            if color not in color_brightness:
                print(f"Warning: Color '{color}' not found, using white.")
                color = white
                brightness = self.default_brightness
            else:
                brightness = level if level is not None else color_brightness[color]
                color = eval(color)  # Convert string to predefined tuple
        else:
            brightness = level if level is not None else self.default_brightness
        
        # Apply brightness to color
        color_with_brightness = self.apply_brightness(color, brightness)
        
        # If reset is False, blend the new color with the existing one
        if not reset:
            current_color = self.strip[pixel_id]
            color_with_brightness = self.blend_colors(current_color, color_with_brightness)
        
        self.strip[pixel_id] = color_with_brightness
        self.strip.write()
        return color_with_brightness, pixel_id

# Create a global instance of the NeoPixelController
_controller = NeoPixelController()

# Expose the setNeo function for direct use
setNeo = _controller.setNeo

"""
v1.0

    - Creates a controller instance with init
    - chagne brightess
    - default brighess from color-brightness table
    
    usage
    from espNeoPixelClass import NeoPixelController as npc, r,g,b,w
    np = npc() # brigtnes slevel, num_pixles and pin (all have defaults)
    np.setNeo(color) # only requires color, level(global default 0-100), pixel id(0), and reset (True) have defaults
    np.setNeo("green")
    setNeo = np.setNeo ( maps it so just needing to use setNeo)
    setNeo(r) makes it red with defualt color from mapping
    
"""



"""


from neopixel import NeoPixel
from machine import Pin
from time import sleep

numOfPixels = 5
pinNumber = 48
defaultBrightness = 10

# Define RGB colors
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
off = (0, 0, 0)

b = "blue"
g = 'green'
r = 'red'
w = 'white'

# Global dictionary to store brightness levels for each color
color_brightness = {
    "red": 80,
    "green": 100,
    "blue": 10,
    "white": 15,
}

class NeoPixelController:
    def __init__(self, brightness_level: int = defaultBrightness, num_pixels: int = numOfPixels, pin: int = pinNumber) -> None:
       \"""
        Initialize the NeoPixelController with default brightness and configuration.
        
        Args:
            brightness_level (int): Default brightness level for NeoPixels (default is 50).
            num_pixels (int): Number of NeoPixels in the strip (default is 5).
            pin (int): Pin number for the NeoPixel data line (default is 4).
        \"""
        self.strip = NeoPixel(Pin(pin), num_pixels)
        self.default_brightness = brightness_level


    def apply_brightness(self, color, level):
        \"""
        Adjust color brightness by scaling RGB values.
        
        Args:
            color (tuple): RGB color.
            level (int): Brightness level (0-100).
            
        Returns:
            tuple: Adjusted RGB color.
       \"""
        scale = level / 100
        return tuple(int(c * scale) for c in color)
    
    def blend_colors(self, color1, color2):
        \"""
        Blend two RGB colors by averaging their values.
        \"""
        return tuple((c1 + c2) // 2 for c1, c2 in zip(color1, color2))
    
        
    def setNeo(self, color, level=None, pixel_id=0, reset=True):
        \"""
        Set a NeoPixel to a specific color and brightness level.
        
        Args:
            color (str or tuple): Color name as a string ("red", "green", etc.) or RGB color tuple.
            level (int, optional): Brightness level. Defaults to None.
            pixel_id (int, optional): Pixel index to set. Defaults to 0.
            reset (bool, optional): Whether to reset all pixels to off. Defaults to False.
        \"""
        if reset:
            self.strip.fill(off)
        
        # Handle color input (name or tuple)
        if isinstance(color, str):
            if color not in color_brightness:
                print(f"Warning: Color '{color}' not found, using white.")
                color = white
                brightness = self.default_brightness
            else:
                brightness = level if level is not None else color_brightness[color]
                color = eval(color)  # Convert string to predefined tuple
        else:
            brightness = level if level is not None else self.default_brightness
        
        # Apply brightness to color
        color_with_brightness = self.apply_brightness(color, brightness)
        
        # If reset is False, blend the new color with the existing one
        if not reset:
            current_color = self.strip[pixel_id]
            color_with_brightness = self.blend_colors(current_color, color_with_brightness)
        
        
        self.strip[pixel_id] = color_with_brightness
        self.strip.write()
        return color_with_brightness, pixel_id

if __name__ == '__main__':
    controller = NeoPixelController(brightness_level=30)
    controller.setNeo("white",30)  # Uses greenBrightness (20%)
    #sleep(.5)
    controller.setNeo(b, reset=True)  # Uses level 50%
    #print(controller.setNeo((255, 255, 0)))  # Uses default brightness (100%)
"""
