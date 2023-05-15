"""
On vous donne deux tableaux d'entiers nums1et nums2. Nous ecrivons les nombres
entiers de nums1et nums2(dans l'ordre ou ils sont donnes) sur deux lignes horizontales distinctes.

On peut tracer des lignes de liaison :
une ligne droite reliant deux nombres nums1[i]et nums2[j]telle que :
nums1[i] == nums2[j], et
la ligne que nous tracons ne croise aucune autre ligne de connexion (non horizontale).
Notez qu'une ligne de connexion ne peut pas se croiser meme aux extremites (c'est-a-dire
que chaque nombre ne peut appartenir qu'a une seule ligne de connexion).
Renvoie le nombre maximum de lignes de connexion que nous pouvons tracer de cette maniere .

contrainte:
=> 1 <= nums1.length, nums2.length <= 500
=> 1 <= nums1[i], nums2[j] <= 2000
"""

class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        if 1<= len(nums1) & len(nums2)<=500:
            pass


#a = [2,5,1,2,5]
#b = [10,5,2,1,5,2]
a = [1,4,2]
b = [1,4,2]
i,j,nb =0,0,0
while i < len(a):
    print("i =", i)
    while j<len(b) and a[i] != b[j]:
        print("j quand a[i] != a[j]",j)
        j += 1

    if j< len(b):
        nb += 1
        print("j quand a[i] == a[j]",j)
        print("nb  ",nb)
        print("*********************")
        if i != j:
            i = j
        else:
            i += 1
    else:
        i += 1


#s = Solution()
#s.maxUncrossedLines(a,b)