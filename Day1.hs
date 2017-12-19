import Data.Char

main = do
  given <- getLine
  putStrLn (show (solve given))

solve (x:xs) = if x == (last xs) then helper xs (digitToInt x) else helper xs 0
  where
    helper [] count = count
    helper [x] count = count
    helper (x:xs:xss) count = if x == xs then helper (xs:xss) (count + digitToInt x) else helper (xs:xss) count
