import yaml
import logging

class Config( object ):
	def __init__( self, filename):
		with open(filename, 'r') as stream:
		    try:
		        self.config = yaml.load(stream)
		    except yaml.YAMLError as exc:
		    	logging,info(exc)

	def getLink( self ):
		return self.config['source']['link']

	def getSourceClass( self ):
		return self.config['source']['class']