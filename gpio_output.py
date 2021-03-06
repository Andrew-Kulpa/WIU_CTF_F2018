import gpiozero, sys, time

#relay + port number
RELAY_PIN = 20

# create a relay object.
# Triggered by the output pin going low: active_high=False.
# Initially off: initial_value=False        COPIED FROM https://gist.github.com/johnwargo/ea5edc8516b24e0658784ae116628277

relay = gpiozero.OutputDevice(RELAY_PIN, active_high=False, initial_value=False)

def set_relay(status):
    if status:
        print("Setting relay: ON")
        relay.on()
    else:
        print("Setting relay: OFF")
        relay.off()


def toggle_relay():
    print("toggling relay")
    relay.toggle()


def main_loop():
    # start by turning the relay off
    set_relay(False)
    while 1:
        # then toggle the relay every second until the app closes
        toggle_relay()
        # wait a second 
        time.sleep(1)


if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        # turn the relay off
        set_relay(False)
        print("\nExiting application\n")
        # exit the application
        sys.exit(0)

