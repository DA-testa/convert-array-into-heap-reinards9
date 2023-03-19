def process():
  
  threads = [0] * threadss
  output = []
  for laiks in darbii:
   
    threadP = threads.index(min (threads) )
    
    output.append(( threadP, threads[threadP] ) )
    
    threads[threadP ] += laiks

  assert darbi == len(output   )

  print("\n".join( [f"{thread_num} {starts_at}" for thread_num, starts_at in output] ) )

threadsJ = input().split(" "  )


threadss = int(threadsJ[0] )


darbi = int(threadsJ[1])    


darbii = [ int(darbs) for darbs in input().split(" ") ]

process()

