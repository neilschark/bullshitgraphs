import io
from bullshitgraphs import bullshitgraphs
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from flask import Flask, Response


BASE_FILENAME="develop"
OUTPUT_TYPE="png"

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # a simple page that says hello
    @app.route('/')
    def show_figures():
        #fig = bullshitgraphs.create_pie_chart(keywords, BASE_FILENAME, OUTPUT_TYPE)
        fig = bullshitgraphs.create_pie_chart(["test", "test2"])
        output = io.BytesIO()
        FigureCanvas(fig).print_png(output)
        return Response(output.getvalue(), mimetype='image/png')

        
        #keywords = []
        #for i, element in enumerate(5):
        #    if i == 0:
        #        continue
        #    keywords.append(element)
#
        #print(f"Your important {len(keywords)} keywords are: {keywords}")
#
        #bullshitgraphs.create_bar_chart(keywords, BASE_FILENAME, OUTPUT_TYPE)
        #bullshitgraphs.create_pie_chart(keywords, BASE_FILENAME, OUTPUT_TYPE)
#
        #print("Your important graphs were created")
        #return 'Hello, World!'

    return app