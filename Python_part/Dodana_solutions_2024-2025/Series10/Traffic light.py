class TrafficLight:

    def __init__(self, initial_state='red'):
        if initial_state not in {'red', 'orange', 'green'}:
            raise ValueError("Invalid state. State must be 'red', 'orange', or 'green'.")
        self.state = initial_state

    def __str__(self):
        return self.state

    def __repr__(self):
        return f"TrafficLight('{self.state}')"

    def next(self):
        if self.state == 'red':
            self.state = 'green'
        elif self.state == 'green':
            self.state = 'orange'
        elif self.state == 'orange':
            self.state = 'red'
