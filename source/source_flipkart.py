from source_base import *

class SourceFlipKart( SourceBase ):
	def extractData( self ):
		details = dict()
		soup = self.getSoupObject()
		details["item"] = soup.find('h1','_3eAQiD').get_text().encode('ascii', 'ignore')
		details["price"] = soup.find('div','_1vC4OE _37U4_g').get_text().encode('ascii', 'ignore')
		return details
