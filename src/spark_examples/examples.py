from lib.session import Session

class SparkExamples:
    def __init__(self):
        self.spark = Session("SparkExamples").get()


    def get_empty_lines(self):
        count_of_empty_lines = self.spark.sparkContext.accumulator(0)

        def blank_lines(line):
            if(len(line) == 0):
                count_of_empty_lines.add(1)
        
        file = self.spark.sparkContext.textFile("/opt/resources/Sample_data.txt")

        r1 = file.foreach(lambda x: blank_lines(x))

        print("Count of empty lines : " ,count_of_empty_lines.value)
    

if __name__ == "__main__":
    se = SparkExamples()
    se.get_empty_lines()
