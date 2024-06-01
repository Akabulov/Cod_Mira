

class CV:
    def __init__(self):
        self.first_name: str = ''
        self.last_name: str = ''
        self.location: str = ''
        self.citizenship: str = ''

        self.desired_position: str = ''

        self.stack_flow: list = []

        self.experience_years: int = 0

        self.degree: str = ''

        self.certificates: list = []

        self.open_source_engagement: list = []

        self.competetive_history: list = []

    def parse_cv(self, filepath):
        pass

    @staticmethod
    def relevancy_predict(stack, *args):
        relevancy = 100
        for technology in args:
            if technology not in stack:
                relevancy -= len(args)/100
        return relevancy

