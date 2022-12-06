#!/bin/bash

for i in {1..99..2}
do
  echo "$i"
done

read name
echo "The name you have entered is $name"  

read a
read b
echo $[a+b]
echo $[a-b]
echo $[a*b]
echo $[a/b]

read x
read y
if [[ $x<$y ]]
then
    echo "X is less than Y"
elif [[ $x>$y ]]
then
    echo "X is greater than Y"
else
    echo "X is equal to Y"
fi

read X
read Y
read Z
if [[ "$X" == "$Y" && "$X" == "$Z" ]] ;
then
    echo 'EQUILATERAL'
elif [[ "$X" == "$Y" || "$X" == "$Z" || "$Y" == "$Z" ]] ;
then
    echo 'ISOCELES'
else
    echo 'SCALENE'
fi

read X
read Y
read Z

if [[ "$X" == "$Y" && "$X" == "$Z" ]]; then
    echo 'EQUILATERAL'
elif [[ "$X" == "$Y" || "$X" == "$Z" || "$Y" == "$Z" ]] ; then
    echo 'ISOSCELES'
else
    echo 'SCALENE'
fi