import justpy as jp

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text='Analysis of Course Reviews', classes='text-h3 text-center q-pa-md')
    p1 = jp.QDiv(a=wp, text='There graphs represent course review analysis')

    return wp

jp.justpy(func=app)