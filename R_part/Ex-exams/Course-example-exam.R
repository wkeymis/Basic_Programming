library(ggplot2)

data("diamonds")

diamonds_small <- head(diamonds, 5000)

dim(diamonds_small)

diamonds_small$cut_new <- ifelse(diamonds_small$cut %in% c("Ideal", "Premium"), "Above average",
                                 ifelse(diamonds_small$cut=="Very Good", "Very good",
                                        "Below average"))

table(diamonds_small$cut, diamonds_small$cut_new)

diamonds_2 <- diamonds_small[, c("price", "carat", "cut_new", "color", "clarity")]

head(diamonds_2)

write.table(diamonds_2, file = "diamonds.txt", row.names = FALSE)
diamonds_check <- read.table("diamonds.txt", header = TRUE)
head(diamonds_check)

library(dplyr)

results <- diamonds_2 %>%
  group_by(color, cut_new) %>%
  summarise(avg_price = mean(price))

print(results)

combine <- diamonds_2 %>%
  left_join(results, by = c("color", "cut_new"))

head(combine)

ggplot(diamonds_2, aes(x=color, y=price)) +
  geom_boxplot(fill="green", coef = 0.5) +
  stat_summary(fun = mean, geom = "point", color = "red", size=3)
fun1 <- function(x){
  if(x >= 0){
    "Non-negative number"
  } else{
    "negative number"
  }
}

fun1(9)
fun1(-9)


