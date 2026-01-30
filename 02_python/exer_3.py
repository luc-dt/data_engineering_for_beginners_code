class Pipeline:

    def __init__(self, pipeline_type):
        self.pipeline_type = pipeline_type          # called an object variable, will be specific for individual objects
    
    def extract(self):
        print(f'Data is being extracted  for {self.pipeline_type}')

    def transform(self):
        print(f'Data is being transformed for {self.pipeline_type}')
    
    def load(self):
        print(f'Data is being loaded for {self.pipeline_type}')

    def run(self):
        self.extract()
        self.transform()
        self.load()

p1 = Pipeline('customer_pipeline')              # we create an object of type Pipeline class
p2 = Pipeline('orders_pipeline')                # we create another object of type Pipeline class

p1.run()                                        # note how the extract, transform and load methods will print customer pipeline
print('-----------------------------------------------')
p2.run()