vec <- sample(c("H", "T"), size = 10, replace = TRUE)

nhead <- 0
position <- NA

for(i in seq_along(vec)){
  if(vec[i] == "H"){
    nheads <- nheads + 1
  } else{
    nheads <- 0
  }
  if(nheads == 3){
    position <- i
    break
  }
}

flip <- function(n = 50){
  vec <- sample(c("H", "T"), size = n, replace = TRUE)
  nheads <- 0
  position <- NA

  for(i in seq_along(vec)){
    if(vec[i] == "H" ){
      nheads <- nheads + 1
    } else{
      nheads <- 0
    }
    if(nheads == 3){
      position <- i
      break
    }
  }
  return(position)
}

flip(10)


library(dplyr)
hotel_data <- read.csv("hotel_sample.csv")

hotel_small <- hotel_data %>%
  select(hotel,adr, arrival_date_month)

hotel_small <- hotel_data %>%
  mutate(
    hotelname = substr(hotel, 1, 6),
    month = match(arrival_date_month, month.name)
  )

result <- hotel_small %>%
  group_by(hotelname, month) %>%
  summarise(Avg_adr = mean(adr))

result2 <- hotel_data %>%
  select(hotel, adr, arrival_date_month) %>%
  mutate(
    hotelname = substr(hotel, 1, 6),
    month = match(arrival_date_month, month.name)
  ) %>%
  group_by(hotelname, month) %>%
  summarise(Avg_adr = mean(adr))

library(ggplot2)

ggplot(result2, aes(x = month, y = Avg_adr, color = hotelname)) +
  geom_point() +
  geom_line() +
  geom_smooth(se = FALSE, method = "loess") +
  theme_bw() +
  labs(
    x = "Month",
    y = "Average daily rate",
    title = "YourName - ADR by month"
  )
