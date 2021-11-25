 #Exercise 4

#Solve the following equations in __F__~97~ (again, assume ⋅ and exponentiation are field pass:[<span class="keep-together">versions</span>]):

* 95 ⋅ 45 ⋅ 31
* 17 ⋅ 13 ⋅ 19 ⋅ 44
* 12^7^ ⋅ 77^49^
# end::exercise4[]
# tag::answer4[]
>>> prime = 97
>>> print(95*45*31 % prime)
23
>>> print(17*13*19*44 % prime)
68
>>> print(12**7*77**49 % prime)
63

# end::answer4[]