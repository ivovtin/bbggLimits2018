#!/bin/bash/
#list=( 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80)
#list=( 1 6 11 16 18 21 26 28 31 34 35 36 37 38 39 41 44 46 48 51 53 56 61 66 71 76 80 )
list=( 36 )  

for ext in ${list[@]}
do
  echo "Processing KL=" $ext
  sed -e 's/\(KL\)\([0-9][0-9]\)/\1'${ext}'/' runKL_.sh >runKL.sh
  sed -e 's/\(KL\)\([0-9][0-9]\)/\1'${ext}'/' bbggLTMaker_KL.h >bbggLTMaker.h 
  sed -e 's/KL/'${ext}'/' bbggLTMaker_KL.C >bbggLTMaker.C 
  . ./runKL.sh
done
