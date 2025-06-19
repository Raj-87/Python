import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        # If more balls are requested than available, return all and empty the hat
        if num_balls >= len(self.contents):
            all_balls = self.contents.copy()
            self.contents.clear()
            return all_balls

        # Randomly draw balls without replacement
        drawn = random.sample(self.contents, num_balls)
        for ball in drawn:
            self.contents.remove(ball)
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    for _ in range(num_experiments):
        # Create a deep copy of the hat for each experiment
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)

        # Count the balls that were drawn
        drawn_counts = {}
        for color in drawn_balls:
            drawn_counts[color] = drawn_counts.get(color, 0) + 1

        # Check if all expected balls are present in the drawn result
        success = True
        for color, count in expected_balls.items():
            if drawn_counts.get(color, 0) < count:
                success = False
                break

        if success:
            success_count += 1

    # Return the estimated probability
    return success_count / num_experiments


# Example usage
if __name__ == "__main__":
    hat = Hat(black=6, red=4, green=3)
    probability = experiment(
        hat=hat,
        expected_balls={'red': 2, 'green': 1},
        num_balls_drawn=5,
        num_experiments=2000
    )
    print(f"Estimated Probability: {probability}")
