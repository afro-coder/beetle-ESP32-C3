from machine import Pin, I2C
import ssd1306

if __name__ == "__main__":
    i2c = I2C(sda=Pin(9), scl=Pin(4))
    display = ssd1306.SSD1306_I2C(128, 64, i2c)
    display.fill(0)

    #display.fill_rect(0,0, 12, 34, 1)
    #display.fill_rect(2, 2, 28, 28, 0)
    #display.vline(9, 8, 22, 1)
    #display.vline(16, 2, 22, 1)
    #display.vline(23, 8, 22, 1)
    #display.fill_rect(4,4, 12, 23, 1)
    display.text('Leon Nunes', 40, 0, 1)
    display.text('Technical', 40, 12, 1)
    display.text('Support',40,24,1)
    display.text('Solo.io',40,36,1)
    display.show()
