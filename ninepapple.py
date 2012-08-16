from __future__ import division

import numpy

class SOM:
"""
A self-organizing map from one space to another
"""
    def __init__(self, sourcedim, targetdim=2, resoltion=16, falloff=3):
        self.sourcedim = sourcedim
        self.targetdim = targetdim
        self.res = resolution # resolution of the map
        self.falloff = falloff # sites will be modified with a linear falloff cone with this radius.
        # TODO implement a decaying falloff over time.
        self.pull = 0.1 # how much the sites are pulled toward trained points in HD space [0.0 - 1.0]
        self.somap = numpy.random.normal(1, 0.2, (self.res, self.res, self.sourcedim))
        # TODO initialize the map using evenly spaced points from the subspace of the targetdim largest principal component eigenvectors
                
    def locate(self,hdpoint):
        # return the ld location of the map site which hdpoint is closest to in hd space 
        # TODO use a kd-tree for faster search
        target = None
        return target
                
    def learnpoints(self,vectors):
        """ vectors should have shape (n, sourcedim) 
            where n is the number of points you want to train
            you can train as many as you want in one call, but you might want to show progress so don't do too many """
        n = len(vectors)
        for i in xrange(n):
            v = vectors[i]
            # find the map site with the closest location in the HD space
            target = self.locate(v)
            # move the map sites in the nearby LD space closer to the target in HD space.
            # self.somap[nbloc] = v*self.pull + siteabs*(1-self.pull)
            

