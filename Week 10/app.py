{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6b4473b5",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'scraping'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-3fe6a1a34277>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mflask\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mFlask\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mrender_template\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mredirect\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl_for\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mflask_pymongo\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mPyMongo\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mscraping\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'scraping'"
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
   "id": "1e57781f",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "61075066",
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
   "execution_count": 4,
   "id": "5a150517",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/\")\n",
    "def index():\n",
    "   mars = mongo.db.mars.find_one()\n",
    "   return render_template(\"index.html\", mars=mars)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "75249eff",
   "metadata": {},
   "outputs": [
    {
     "ename": "AssertionError",
     "evalue": "View function mapping is overwriting an existing endpoint function: scrape",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAssertionError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-7-def9374392f4>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;33m@\u001b[0m\u001b[0mapp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mroute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"/scrape\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0mscrape\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m    \u001b[0mmars\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mmongo\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdb\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmars\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m    \u001b[0mmars_data\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mscraping\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mscrape_all\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m    \u001b[0mmars\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mupdate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m{\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmars_data\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mupsert\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\app.py\u001b[0m in \u001b[0;36mdecorator\u001b[1;34m(f)\u001b[0m\n\u001b[0;32m   1313\u001b[0m         \u001b[1;32mdef\u001b[0m \u001b[0mdecorator\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mf\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1314\u001b[0m             \u001b[0mendpoint\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0moptions\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpop\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"endpoint\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1315\u001b[1;33m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0madd_url_rule\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mrule\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mendpoint\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0moptions\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1316\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1317\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\app.py\u001b[0m in \u001b[0;36mwrapper_func\u001b[1;34m(self, *args, **kwargs)\u001b[0m\n\u001b[0;32m     96\u001b[0m                 \u001b[1;34m\"before the application starts serving requests.\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     97\u001b[0m             )\n\u001b[1;32m---> 98\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     99\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    100\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0mupdate_wrapper\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mwrapper_func\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\app.py\u001b[0m in \u001b[0;36madd_url_rule\u001b[1;34m(self, rule, endpoint, view_func, provide_automatic_options, **options)\u001b[0m\n\u001b[0;32m   1282\u001b[0m                 raise AssertionError(\n\u001b[0;32m   1283\u001b[0m                     \u001b[1;34m\"View function mapping is overwriting an \"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1284\u001b[1;33m                     \u001b[1;34m\"existing endpoint function: %s\"\u001b[0m \u001b[1;33m%\u001b[0m \u001b[0mendpoint\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1285\u001b[0m                 )\n\u001b[0;32m   1286\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mview_functions\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mendpoint\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mview_func\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAssertionError\u001b[0m: View function mapping is overwriting an existing endpoint function: scrape"
     ]
    }
   ],
   "source": [
    "@app.route(\"/scrape\")\n",
    "def scrape():\n",
    "   mars = mongo.db.mars\n",
    "   mars_data = scraping.scrape_all()\n",
    "   mars.update({}, mars_data, upsert=True)\n",
    "   return redirect('/', code=302)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "2d935a32",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'mars' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-8-88cd6407df77>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mmars\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mupdate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m{\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmars_data\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mupsert\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[1;32mreturn\u001b[0m \u001b[0mredirect\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'/'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcode\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m302\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'mars' is not defined"
     ]
    }
   ],
   "source": [
    "mars.update({}, mars_data, upsert=True)\n",
    "return redirect('/', code=302)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "26a87e56",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "   app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "01ac3a02",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
   "version": "3.7.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
