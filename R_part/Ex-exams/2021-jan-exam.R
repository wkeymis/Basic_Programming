x <- 1

n2 <- x - x^3/factorial(3)
n3 <- x - x^3/factorial(3) + x^5/factorial(5)

n2
n3

sin(1)

sin_approx_loop <- function(n, x){
  approx_val <- 0
  for(k in 0:(n-1)){
    term <- ((-1)^k * x^(2*k + 1)) / factorial(2*k + 1)
    approx_val <- approx_val + term
  }
  data.frame(n = n, x = x, approx = approx_val)
}

sin_approx_loop(5,2)

set.seed(123)
business <- data.frame(
  business_status = sample(1:4, 20, replace = TRUE),  # some invalid 4's
  sex             = sample(c("M","F",NA), 20, replace = TRUE),
  neoconsc        = sample(20:50, 20, replace = TRUE),
  neoopen         = sample(10:40, 20, replace = TRUE)
)
head(business)

sum(is.na(business$business_status))
sum(is.na(business$sex))
library(dplyr)

sub1 <- business %>%
  mutate(business_status = ifelse(business_status %in% 1:3, business_status, NA))

sub2 <- sub1 %>% filter(neoconsc > 30)

library(ggplot2)

ggplot(sub2, aes(x = neoopen, y = neoconsc, color = factor(business_status))) +
  geom_point(size = 3) +
  theme_bw() +
  labs(
    title = "neoopen vs neoconsc by business_status",
    color = "Business_status"
  )

business %>%
  mutate(business_status = ifelse(business_status %in% 1:3, business_status, NA)) %>%
  filter(neoconsc > 30) %>%
  ggplot(aes(x = neoopen, y = neoconsc, color = factor(business_status))) +
  geom_point(size = 3) +
  theme_bw()

plot1 <- ggplot(
  remove_missing(sub2, vars = "business_status"),
  aes(x = neoopen, y = neoconsc, color = factor(business_status))
) +
  geom_point(size = 3) +
  theme_bw()

library(ggExtra)
ggMarginal(plot1, type = "boxplot")
