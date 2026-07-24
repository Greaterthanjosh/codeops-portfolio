def getOnlyEvens (arr):
   result = []

   for i in range(len(arr)):
      if i % 2 == 0 and arr[i] % 2 == 0:
         result.append(arr[i])

   print(result)

# Test 1
getOnlyEvens([1, 2, 3, 6, 4, 8])  

# Test 2
getOnlyEvens([0, 1, 2, 3, 4])

def reverseCompare(num):
   tens = num // 10
   ones = num % 10

   revesed_num = ones * 10 + tens

   if num > revesed_num:
      print("ok")
   else:
      print("Not ok")


# Test 1
reverseCompare(72)

# Test 2
reverseCompare(23)

def returnfactorial(num):
    factorial = 1

    for i in range(1, num + 1):
       factorial *= i

    return factorial

# Test 1
print(returnfactorial(5))

# Test 2
print(returnfactorial(6))

# Test 3
print(returnfactorial(0))

def checkMeera(arr):
   for num in arr:
      if num * 2 in arr:
         print("I am NOT a Meera array")
         return

   print("I am a Meera array")


# Test 1
checkMeera([10, 4, 0, 5]) 

# Test 2
checkMeera([7, 4, 9])

# Test 3
checkMeera([1, -6, 4, -3])

def isDual(arr):
    counts = {}

    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    for count in counts.values():
        if count != 2:
            return 0

    return 1


# Test cases
print(isDual([1, 2, 1, 3, 3, 2]))   
print(isDual([2, 5, 2, 5, 5]))      
print(isDual([3, 1, 1, 2, 2]))

def digitalClock(seconds):
    seconds = seconds % 86400  # Wrap around after 24 hours

    hours = seconds // 3600
    seconds = seconds % 3600

    minutes = seconds // 60
    seconds = seconds % 60

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


# Test cases
print(digitalClock(5025))    
print(digitalClock(61201))   
print(digitalClock(87000))
