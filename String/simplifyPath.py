class Solution(object):

    
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        outpath = [] #start with a / 
         
        lst = [p for p in path.split("/") if p]

        #return lst

        # outpath.append("/")

        for item in lst:
            if item == "..":
                if outpath:
                    outpath.pop()
            elif item == ".":
                continue
            else:
                outpath.append(item)



        return "/" + "/".join(outpath)
            
