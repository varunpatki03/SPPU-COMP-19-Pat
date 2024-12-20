def accept_array(A):  

   n = int(input("Enter the total no. of student : ")) 

   for i in range(n): 

      x = float(input("Enter the  first year percentage of student %d : "%(i+1))) 

      A.append(x) 

   print("Array accepted successfully\n\n"); 

def display_array(A):  

   n = len(A) 

   if(n == 0) : 

      print("\nNo records in the database") 

   else : 

      print("Array of FE Marks : ",end=' ') 

      for i in range(n) : 

         print("%.2f  "%A[i],end=' ') 

      print("\n"); 


def Selection_sort(A) : 

   temp=0 

   n = len(A) 

   for i in range(n-1):  # correct position to copy smallest element 

      min_ind = i 

      for j in range(i + 1, n) : # to find smallest element 

         if(A[j] < A[min_ind]) : 

            min_ind = j 

      temp = A[i] 

      A[i] = A[min_ind] 

      A[min_ind] = temp 

  

def Bubble_sort(A) : 

    temp=0 

    print("Bubble sort passwise output is: ") 

    for i in range(len(A)-1): 

        for j in range (len(A)-i-1): 

            if(A[j]<A[j+1]): 

                temp=A[j] 

                A[j]=A[j+1] 

                A[j+1]=temp 

       

def Main() :    

   A = [] 

   while (1) : 

      print ("\t1 : Accept & Display the FE Marks") 

      print ("\t2 : Selection Sort Ascending order") 

      print ("\t3 : Bubble sort Descending order and display top five scores") 

      print ("\t4 : Exit") 

      ch = int(input("Enter your choice : ")) 

      if (ch == 4): 

         print ("End of Program") 

         quit() 

      elif (ch==1): 

         accept_array(A) 

         display_array(A) 

      elif (ch==2): 

         print("Marks before sorting") 

         display_array(A) 

         Selection_sort(A) 

         print("Marks after sorting") 

         display_array(A) 

      elif (ch==3): 

         print("Marks before sorting") 

         display_array(A) 

         Bubble_sort(A) 

         print("Marks after sorting") 

         display_array(A) 

         if(len(A) >= 5) : 

            print("Top Five Scores : ") 

            for i in range(5) : 

               print("\t%.2f"%A[i]) 

         else : 

            print("Top Scorers : ") 

            for i in range(len(A)) : 

               print("\t%.2f"%A[i])                   

      else : 

           print ("Wrong choice entered !! Try again") 

Main() 
