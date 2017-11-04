import abc
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests



ua = UserAgent()
BROWSER = [ ua.chrome, ua.firefox ]
HEADER  = { 'UserAgent': ua.firefox }

class SourceBase( object) :
	def __init__( self, link):
		self.link = link
		self.browser = 0

	def getSoupObject( self ):
		res = self.getResponse()
		soup = BeautifulSoup(res.content, "html.parser")
		return soup

	def getResponse( self ):
		''' get response  '''
		try:
			res = requests.get( self.link, headers={ 'UserAgent': BROWSER[ self.browser] } )
			if res.status_code == 503:
				logging.error( " Try again with a different browser ")
				self.browser  = self.browser % len(BROWSER)
			elif res.status_code != 200:
				res = ""
		except Exception as e:
			logging.error( " Request to the {} failed".format(str(e))  )
		return res

	@abc.abstractmethod
	def extractData( self ):
		''' extract product details from the response '''
		return {}

	__metaclass__ = abc.ABCMeta