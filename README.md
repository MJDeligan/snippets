Python snippets
===============

### Includes different, interesting concepts that can be used in Python, which are sometimes more, sometimes less useful.  
# Overview  
## Functional  
- Curry decorator, which makes any function (with determined arguments) into a curried one
  - Read why about [currying](https://wiki.haskell.org/Currying#:~:text=Currying%20is%20the%20process%20of,the%20rest%20of%20that%20tuple.) is useful 
  - Also includes some explanations in the code
- partial map, relating to the concept of currying, partial map is a map function with a preset function to be mapped to the iterable
## BTree
- Normal Binary tree implementation, including post-pre-and inorder representation and **inverting**
- AVLTree aka self balancing tree, which avoids the risk of becoming a degenerate tree for which usual O(logn) operation are O(n)
## Prototype  
- A little script to illustrate how prototyping for class-specific operators can be generalised to extend what is already present in python
