from source_base import *

class SourceAmazon( SourceBase ):
	def extractData( self ):
		details = dict()
		soup = self.getSoupObject()
		details["item"] = soup.find("span", {"id": "productTitle" }).getText().strip().encode('ascii', 'ignore')
		try:
			details["price"] = soup.find("span", {"id": "priceblock_ourprice" }).getText().strip().encode('ascii', 'ignore')
		except:
			details["price"] = soup.find("span", {"id": "priceblock_saleprice" }).getText().strip().encode('ascii', 'ignore')
		return details
