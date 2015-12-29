import flask
from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
from HtmlClarifai2DArray import *
# index view function suppressed for brevity


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def input():
    form = LoginForm()
    if form.validate_on_submit():
          flash('Login requested for OpenID="%s", remember_me=%s' %
                (form.openid.data, str(form.remember_me.data)))
          return redirect('/clarifai?login=%s' % form.openid.data)
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])

@app.route('/clarifai', methods=['GET', 'POST'])
def images():
        openid = flask.request.args.get('login')
#        ret = flask.request.args.get('login')
#        print '*******'
#        print type(ret)
#        print ret
#        print '*******'
#        return ret

	#keywords = HtmlClarifai2DArray("kellylpt")
	#clari = HtmlClarifai2DArray("kellylpt")
	clari = HtmlClarifai2DArray(openid)
        
        
        response = urllib2.urlopen(clari.ig_username(openid), timeout=20)
        print '2----------- response'
        print response
        print '2-----------'
        insta_html = response.read()
        insta_keywords = clari.get_keywords(clari.get_sources(insta_html))
        
        print '11----------------'
        print insta_keywords
        print type(insta_keywords)
        print '11----------------'
        
        return ','.join(insta_keywords[0])
#############################################
         


        response = urllib2.urlopen(HtmlClarifai2DArray.ig_username(openid), timeout=10)
        print '2----------- response'
        print response
        print '2-----------'
        insta_html = response.read()
        insta_keywords = HtmlClarifai2DArray.get_keywords(HtmlClarifai2DArray.get_sources(insta_html))
        
        print '11----------------'
        print insta_keywords
        print type(insta_keywords)
        print '11----------------'
        
        return ','.join(insta_keywords[0])
        
        

        google_html = "https://photos.google.com/share/AF1QipONERd0AGm-CcUrQ_m56P4R0eypHJDNDLslYs0mrw_KWuLDtzxii6cE_rY7luRxqw?key=X0x3QWFlYmVCQlgtZGgzcFoycGhldWVYVjNzSGd3"
        google_sources = HtmlClarifai2DArray.return_photo_url(google_html)
        google_keywords = HtmlClarifai2DArray.get_keywords(google_sources)
        keywords = google_keywords
        print '-------999999999----'
	print keywords
	print type(keywords[0])
        print '-------999999999----'
	return  ','.join(keywords[0])
