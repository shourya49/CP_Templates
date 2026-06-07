from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

# Actually you have to use yield for accepting results from the recursive call as well for returning the value also. 
# It will be more clear from these examples.

@bootstrap
def recurse(n):
  if (n < 2):
    yield n
  yield (yield recurse(n-1)) + (yield recurse(n-2))
  
@bootstrap
def dfs(node,m):
    visited[node]=1
    if a[node-1]==1:
        m=m+1
    else:
        m=0
    if m>k:
        yield 0
    for v in g[node]:
        if visited[v]!=1:
            yield dfs(v,m) #it was just dfs(v,m) before
    if node in leaf:
        leaf[node]=1
    yield 1
