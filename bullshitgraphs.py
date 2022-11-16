import sys
import os
import random
import matplotlib.pyplot as plt
from typing import List

BASE_FILENAME="develop"
OUTPUT_TYPE="png"

def create_pie_chart(keywords: List[str], base_filename: str, output_type: str):
    data = []
    explode = []
    biggest_value = 0
    biggest_iterator = 0

    for i, _ in enumerate(keywords):
        random_value = random.randint(10, 100)
        data.append(random_value)
        explode.append(0)

        if random_value >= biggest_value:
            biggest_iterator = i
            biggest_value = random_value

    explode[biggest_iterator] = 0.1

    fig1, ax1 = plt.subplots()
    ax1.set_xlabel("Distribution of value")
    ax1.pie(data, explode=explode, labels=keywords, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.savefig(f"outputs/{base_filename}_pie.{output_type}")

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
    create_pie_chart(keywords, BASE_FILENAME, OUTPUT_TYPE)

    print("Your important graphs were created")


if __name__=="__main__":
    main()
