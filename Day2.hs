import Data.Char

main = do
  x <- getAndJoin
  putStrLn (show (checkSum x))

getAndJoin = do
  x <- getLine
  if x == "" then return [] else do 
    xs <- getAndJoin
    return ((combine x [] []):xs)

combine [] accum temp = (read temp :: Int) : accum
combine (x:xs) accum temp = if (x /= '\t') then combine xs accum (temp ++ [x])
  else combine xs ((read temp :: Int) : accum) []

checkSum [] = 0
checkSum (x:xs) = (maximum x - minimum x) + checkSum xs
