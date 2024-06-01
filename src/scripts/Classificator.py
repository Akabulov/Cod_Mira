

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

    def calculate_relevancy(self, **kwargs):
        relevancy = 100
        for technology in kwargs['stack_flow']:
            if technology not in self.stack_flow:
                relevancy -= len(kwargs)/100

        if kwargs['degree'] != self.degree:
            relevancy -= len(kwargs) / 100

        if kwargs['experience_years'] > self.experience_years:
            relevancy -= len(kwargs) / 100

