import sys
import os
import random
import matplotlib.pyplot as plt
from typing import List

BASE_FILENAME="develop"
OUTPUT_TYPE="png"

def create_bar_chart(keywords: List[str], base_filename: str, output_type: str):
    data = []

    for _ in keywords:
        data.append(random.randint(5, 40))

    plt.xlabel('Option')
    plt.ylabel('Annual savings in percent')

    plt.bar(keywords, data)
    plt.savefig(f"outputs/{base_filename}_bar.{output_type}")


def main():
    keywords = []
    for i, element in enumerate(sys.argv):
        if i == 0:
            continue
        keywords.append(element)
            
    print(f"Your important {len(keywords)} keywords are: {keywords}")

    create_bar_chart(keywords, BASE_FILENAME, OUTPUT_TYPE)

    print("Your important graphs were created")


if __name__=="__main__":
    main()
