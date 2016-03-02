module Delenie where
import Data.Ord

splitWords  :: (Char -> Bool) -> String -> [String]
splitWords _ [] = [[]]
splitWords p s = filter (\x -> length x > 0) (reverse(actualSplit p s [[]]))

actualSplit :: (Char -> Bool) -> String -> [String] -> [String]
actualSplit  _ [] a = a
actualSplit p (ch:s) (f:v) = if (p ch) then actualSplit p s ([]:reverse(f):v)
                                       else actualSplit p s ((ch:f):v)
whiteSpace  :: Char -> Bool
whiteSpace ch = not (elem ch (['a'..'z']++['A'..'Z']))
