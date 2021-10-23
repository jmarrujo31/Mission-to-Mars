{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f633b34b",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[WDM] - \n",
      "\n",
      "[WDM] - ====== WebDriver manager ======\n",
      "[WDM] - Current google-chrome version is 94.0.4606\n",
      "[WDM] - Get LATEST driver version for 94.0.4606\n",
      "[WDM] - Get LATEST driver version for 94.0.4606\n",
      "[WDM] - Trying to download new driver from https://chromedriver.storage.googleapis.com/94.0.4606.61/chromedriver_mac64.zip\n",
      "[WDM] - Driver has been saved in cache [/Users/josephmarrujo/.wdm/drivers/chromedriver/mac64/94.0.4606.61]\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, render_template, redirect, url_for\n",
    "from flask_pymongo import PyMongo\n",
    "import scraping"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "216bd4aa",
   "metadata": {},
   "outputs": [],
   "source": [
    "#setup Flask\n",
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "3be1e787",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use flask_pymongo to set up mongo connection\n",
    "app.config[\"MONGO_URI\"] = \"mongodb://localhost:27017/mars_app\"\n",
    "mongo = PyMongo(app)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "40a3f7f9",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/\")\n",
    "def index():\n",
    "   mars = mongo.db.mars.find_one()\n",
    "   return render_template(\"index.html\", mars=mars)\n",
    "\n",
    "\n",
    "@app.route(\"/scrape\")\n",
    "def scrape():\n",
    "   mars = mongo.db.mars\n",
    "   mars_data = scraping.scrape_all()\n",
    "   mars.update({}, mars_data, upsert=True)\n",
    "   return redirect('/', code=302)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "   app.run()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PythonData",
   "language": "python",
   "name": "pythondata"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
