# # doing necessary imports
#
# from flask import Flask, render_template, request, jsonify
# # from flask_cors import CORS,cross_origin
# import requests
# from bs4 import BeautifulSoup as bs
# from urllib.request import urlopen as uReq
# import pymongo
#
# app = Flask(__name__)  # initialising the flask app with the name 'app'
#
#
# # base url + /
# # http://localhost:8000 + /
# @app.route('/', methods=['POST', 'GET'])  # route with allowed methods as POST and GET
# def index():
#     if request.method == 'POST':
#         searchString = request.form['content'].replace(" ", "")  # obtaining the search string entered in the form
#         try:
#             client = pymongo.MongoClient("mongodb://localhost:27017/")  # opening a connection to Mongo
#             db = client['CrawlerDb']  # connecting to the database called crawlerDB
#             reviews = db[searchString].find({})  # searching the collection with the name same as the keyword
#             if reviews.count() > 0:  # if there is a collection with searched keyword and it has records in it
#                 return render_template('results.html', reviews=reviews)  # show the results to user
#             else:
#                 mydb = db[searchString]
#                 flipkart_url = "https://www.flipkart.com/search?q=" + searchString  # preparing the URL to search the product on flipkart
#                 uClient = uReq(flipkart_url)  # requesting the webpage from the internet
#                 flipkartPage = uClient.read()  # reading the webpage
#                 uClient.close()  # closing the connection to the web server
#                 flipkart_html = bs(flipkartPage, "html.parser")  # parsing the webpage as HTML
#                 bigboxes = flipkart_html.findAll("div", {
#                     "class": "_1AtVbE col-12-12"})  # seacrhing for appropriate tag to redirect to the product link
#                 del bigboxes[
#                     0:3]  # the first 3 members of the list do not contain relevant information, hence deleting them.
#                 reviews = []  # initializing an empty list for reviews
#
#                 filename = searchString + ".csv"  # filename to save the details
#                 fw = open(filename, "w", encoding='utf-8')  # creating a local file to save the details
#                 headers = "Product, Customer Name, Rating, Heading, Comment \n"  # providing the heading of the columns
#                 fw.write(headers)  # writing first the headers to file
#
#                 for num_box in bigboxes:
#                     print(num_box)
#                     box = num_box  # taking the first iteration (for demo)
#                     productLink = "https://www.flipkart.com" + box.div.div.div.a[
#                         'href']  # extracting the actual product link
#                     prodRes = requests.get(productLink)  # getting the product page from server
#                     prod_html = bs(prodRes.text, "html.parser")  # parsing the product page as HTML
#                     commentboxes = prod_html.find_all('div', {
#                         'class': "_16PBlm"})  # finding the HTML section containing the customer comments
#
#                     # iterating over the comment section to get the details of customer and their comments
#                     for commentbox in commentboxes:
#                         try:
#                             # name = commentbox.div.div.find_all('p', {'class': '_2V5EHH'})[0].text
#                             name = commentbox.div.div.find_all('div', {'class': 'row _3n8db9'})[0].find('p', {
#                                 'class': '_2sc7ZR _2V5EHH'}).text
#
#                         except:
#                             name = 'No Name'
#
#                         try:
#                             # rating = commentbox.div.div.div.div.text
#                             rating = commentbox.div.div.contents[0].find('div', {'class': '_3LWZlK _1BLPMq'}).text
#
#
#                         except:
#                             rating = 'No Rating'
#
#                         try:
#                             # commentHead = commentbox.div.div.div.p.text
#                             commentHead = commentbox.div.div.contents[0].find_all('p', {'class': '_2-N8zT'})[0].text
#                         except:
#                             commentHead = 'No Comment Heading'
#                         try:
#                             # comtag = commentbox.div.div.find_all('div', {'class': ''})
#                             # custComment = comtag[0].div.text
#                             custComment = commentbox.find('div', {'class': 't-ZTKy'})
#                             custComment = custComment.div.div.text
#                         except:
#                             custComment = 'No Customer Comment'
#
#                         fw.write(
#                             searchString + "," + name.replace(",", ":") + "," + rating + "," + commentHead.replace(",",
#                                                                                                                    ":") + "," + custComment.replace(
#                                 ",", ":") + "\n")
#                         mydict = {"Product": searchString, "Name": name, "Rating": rating, "CommentHead": commentHead,
#                                   "Comment": custComment}  # saving that detail to a dictionary
#
#                         mydb.insert_one(mydict)
#                         reviews.append(mydict)  # appending the comments to the review list
#                 return render_template('results.html', reviews=reviews)  # showing the review to the user
#         except:
#             return 'something is wrong'
#             # return render_template('results.html')
#     else:
#         return render_template('index.html')
#
#
# if __name__ == "__main__":
#     app.run(port=8000, debug=True)  # running the app on the local machine on port 8000




# doing necessary imports

from flask import Flask, render_template, request, jsonify
# from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

app = Flask(__name__)  # initialising the flask app with the name 'app'

@app.route('/',methods=['GET'])
def homepage():
    return render_template('index_H.html')

# base url + /
# http://localhost:8000 + /
@app.route('/scrap', methods=['POST', 'GET'])  # route with allowed methods as POST and GET
def index():
    if request.method == 'POST':
        searchString = request.form['content'].replace(" ", "")  # obtaining the search string entered in the form
        try:

            flipkart_url = "https://www.flipkart.com/search?q=" + searchString  # preparing the URL to search the product on flipkart
            uClient = uReq(flipkart_url)  # requesting the webpage from the internet
            flipkartPage = uClient.read()  # reading the webpage
            uClient.close()  # closing the connection to the web server
            flipkart_html = bs(flipkartPage, "html.parser")  # parsing the webpage as HTML
            bigboxes = flipkart_html.findAll("div", {
                "class": "_1AtVbE col-12-12"})  # seacrhing for appropriate tag to redirect to the product link
            del bigboxes[
                0:3]  # the first 3 members of the list do not contain relevant information, hence deleting them.
            reviews = []  # initializing an empty list for reviews

            for i in range(5):
                # print(i)
                box = bigboxes[i]  # taking the first iteration (for demo)
                productLink = "https://www.flipkart.com" + box.div.div.div.a[
                    'href']  # extracting the actual product link
                prodRes = requests.get(productLink)  # getting the product page from server
                prod_html = bs(prodRes.text, "html.parser")  # parsing the product page as HTML
                commentboxes = prod_html.find_all('div', {
                    'class': "_16PBlm"})  # finding the HTML section containing the customer comments

                # iterating over the comment section to get the details of customer and their comments
                for commentbox in commentboxes:
                    try:
                        name = commentbox.div.div.find_all('div', {'class': 'row _3n8db9'})[0].find('p', {
                            'class': '_2sc7ZR _2V5EHH'}).text

                    except:
                        name = 'No Name'

                    try:

                        rating = commentbox.div.div.contents[0].find('div', {'class': '_3LWZlK _1BLPMq'}).text


                    except:
                        rating = 'No Rating'

                    try:

                        commentHead = commentbox.div.div.contents[0].find_all('p', {'class': '_2-N8zT'})[0].text
                    except:
                        commentHead = 'No Comment Heading'
                    try:

                        custComment = commentbox.find('div', {'class': 't-ZTKy'})
                        custComment = custComment.div.div.text
                    except:
                        custComment = 'No Customer Comment'

                    mydict = {"Product": searchString, "Name": name, "Rating": rating, "CommentHead": commentHead,
                              "Comment": custComment}  # saving that detail to a dictionary

                    reviews.append(mydict)  # appending the comments to the review list
            return render_template('results.html', reviews=reviews)  # showing the review to the user
        except:
            return 'something is wrong in try block'
            # return render_template('results.html')
    else:
        return "Something is wrong in if block"


if __name__ == "__main__":
    app.run(port=8000, debug=True)  # running the app on the local machine on port 8000
