from astrocultivators import app

if __name__ == '__main__':
    host = '130.166.24.225'
    app.run(host=host, port=5000, debug=True)
    # app.run(debug=True) # run local
