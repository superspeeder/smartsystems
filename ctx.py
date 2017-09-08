class Texture(object):
  def __init__(self, name, id_, texturefilename):
    self.texturefilename = texturefilename
    self.name = name
    self.id_ = id_
  def getName(self):
    return self.name
  def getTexture(self):
    return self.texutefilename
  def getId(self):
    return self.id_
  
  
class SmartTexture(Texture):
  def __init__(self,name,id_,texturefilename,tilesettype):
    super(SmartTexture, self).__init__(name,id_,texturefilename)
    self.tilesettype = tilesettype
  def getTileSetType(self):
		return self.tilesettype

	
class ConnectedTexturesConfig(object):
	def __init__(self, **kw):
		for k,v in kw.items():
			setattr(self, k,v)
	
	
class TileMap(object):
	def __init__(self,usenegatives, addcolfornegatives=True, addrowfornegatives=True):
		self.use_negatives = usenegatives
		self.new_cols_for_negative_values = addcolfornegatives
		self.new_rows_for_negative_values = addcolfornegatives
		
