# LOADING PACKAGES AND DATA
library(plyr)
library(dplyr)
library(tidyr)
library(tidyverse)
library(psych)
library(ggplot2)
library(readr)
library(ggpubr)
library(stats)
library(agricolae)

beh_et <- "C:/Users/neoad/Downloads/dibs/dibs/your_todays_version/BehData_correct"
beh_et_file <- list.files(path = beh_et, pattern = "*.csv", full.names = TRUE)
nm1 <- c("type", "latency", "rank", "duration", "sac_amplitude", "sac_angle", "iEvent", "CorScorePair", "CorScoreEvent", "CorScoreDetail", "NrmzMeanConfPair", "NrmzMeanConfEvent", "NrmzMeanConfDetail", "SumCorConfPair", "SumCorConfEvent", "SumCorConfDetail", "PairNCat", "eCorScorePair", "eCorScoreEvent", "eCorScoreDetail", "eNrmzMeanConfPair", "eNrmzMeanConfEvent", "eNrmzMeanConfDetail", "eSumCorConfPair", "eSumCorConfEvent", "eSumCorConfDetail", "iBlock", "iEventPerBlock", "Refi", "Refi2", "NrmzMeanConfPair2bins", "NrmzMeanConfEvent2bins", "NrmzMeanConfDetail2bins", "eNrmzMeanConfPair2bins", "eNrmzMeanConfEvent2bins", "eNrmzMeanConfDetail2bins", "NrmzMeanConfPair_CorRefi", "NrmzMeanConfEvent_CorRefi", "NrmzMeanConfDetail_CorRefi", "eNrmzMeanConfPair_CorRefi", "eNrmzMeanConfEvent_CorRefi", "eNrmzMeanConfDetail_CorRefi", "eNrmzMeanConfPair_EventOnset2bins", "eNrmzMeanConfEvent_EventOnset2bins", "eNrmzMeanConfDetail_EventOnset2bins", "PP")
beh_et_dataset <- setNames(do.call(rbind, Map("cbind", lapply(beh_et_file, read.table, sep = ";"), V4 = beh_et_file)), nm1)
#duplicated_names <- duplicated(colnames(beh_et_dataset))
#beh_et_dataset <- beh_et_dataset[!duplicated_names]

dataset <- beh_et_dataset %>%
  drop_na()
  #filter(type == "fixation")

View(dataset)

# RECODING VARIABLES
dataset$iEvent <- as.numeric(dataset$iEvent)
dataset$iEvent <- ifelse(dataset$iBlock == 2, dataset$iEvent - 15,
    ifelse(dataset$iBlock == 3, dataset$iEvent - 30,
        ifelse(dataset$iBlock == 4, dataset$iEvent - 45,
            dataset$iEvent
        )
    )
)
dataset$iEvent <- as.numeric(dataset$iEvent)

dataset <- dataset %>%
    mutate(iBlock = factor(iBlock, levels = c("1", "2", "3", "4")))
dataset <- dataset %>%
    mutate(iEvent = factor(iEvent, levels = c("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15")))
dataset$NrmzMeanConfPair <- as.numeric(dataset$NrmzMeanConfPair)
dataset$NrmzMeanConfEvent <- as.numeric(dataset$NrmzMeanConfEvent)
dataset$NrmzMeanConfDetail <- as.numeric(dataset$NrmzMeanConfDetail)

dataset <- dataset %>%
    mutate(NrmzMeanConfAll = (NrmzMeanConfPair + NrmzMeanConfEvent + NrmzMeanConfDetail) / 3)
dataset$NrmzMeanConfAll <- as.numeric(dataset$NrmzMeanConfAll)

# ERRORPLOT GRAPHS
ggerrorplot(dataset,
    x = "iBlock", y = "NrmzMeanConfPair",
    desc_stat = "mean_sd", error.plot = "errorbar",
    add = "mean"
)
ggerrorplot(dataset,
    x = "iEvent", y = "NrmzMeanConfPair",
    desc_stat = "mean_sd", error.plot = "errorbar",
    add = "mean"
)

ggerrorplot(dataset,
    x = "iBlock", y = "NrmzMeanConfEvent",
    desc_stat = "mean_sd", error.plot = "errorbar",
    add = "mean"
)
ggerrorplot(dataset,
    x = "iEvent", y = "NrmzMeanConfEvent",
    desc_stat = "mean_sd", error.plot = "errorbar",
    add = "mean"
)

ggerrorplot(dataset,
    x = "iBlock", y = "NrmzMeanConfDetail",
    desc_stat = "mean_sd", error.plot = "errorbar",
    add = "mean"
)
ggerrorplot(dataset,
    x = "iEvent", y = "NrmzMeanConfDetail",
    desc_stat = "mean_sd", error.plot = "errorbar",
    add = "mean"
)

ggerrorplot(dataset,
    x = "iBlock", y = "NrmzMeanConfAll",
    desc_stat = "mean_sd", error.plot = "errorbar",
    add = "mean"
)
ggerrorplot(dataset,
    x = "iEvent", y = "NrmzMeanConfAll",
    desc_stat = "mean_sd", error.plot = "errorbar",
    add = "mean"
)

# MORE DATA MANIPULATION
dataset$PPno <- substr(dataset$PP, 82, 83)
dataset$PPno <- as.numeric(sub("_", "", dataset$PPno))

dataset$cond <- ifelse(dataset$PPno %% 2 == 0, "even",
    "odd"
)
dataset$cond <- as.factor(dataset$cond)

dataset2 <- dataset %>%
    drop_na() %>%
    group_by(iBlock, iEvent, cond) %>%
    summarise_at(
        vars(
            NrmzMeanConfPair, NrmzMeanConfEvent,
            NrmzMeanConfDetail, NrmzMeanConfAll
        ),
        list(name = mean)
    )

# MIXED ANOVAS
anova_pair <- aov(NrmzMeanConfPair_name ~ iBlock + iEvent + cond,
    data = dataset2
)
anova_event <- aov(NrmzMeanConfEvent_name ~ iBlock + iEvent + cond,
    data = dataset2
)
anova_detail <- aov(NrmzMeanConfDetail_name ~ iBlock + iEvent + cond,
    data = dataset2
)
anova_all <- aov(NrmzMeanConfAll_name ~ iBlock + iEvent + cond,
    data = dataset2
)
summary(anova_pair)
summary(anova_event)
summary(anova_detail)
summary(anova_all)

# MORE DETAIL - LINEAR MODELS
mod_pair <- lm(NrmzMeanConfPair_name ~ iBlock + iEvent + cond, data = dataset2)
mod_event <- lm(NrmzMeanConfEvent_name ~ iBlock + iEvent + cond, data = dataset2)
mod_detail <- lm(NrmzMeanConfDetail_name ~ iBlock + iEvent + cond, data = dataset2)
mod_all <- lm(NrmzMeanConfAll_name ~ iBlock + iEvent + cond, data = dataset2)
summary(mod_pair)
summary(mod_event)
summary(mod_detail)
summary(mod_all)

# MAKING DATA FRAME WITH MEMORY SCORES AND FIXATION SUMMARIES
dataset <- dataset %>%
    mutate(
        Refi = factor(Refi),
        PPno = factor(PPno)
    )

x <- tapply(dataset$Refi, dataset$PPno, summary, simplify = T)
y <- data.frame(
    x[["1"]], x[["2"]], x[["3"]], x[["4"]], x[["5"]],
    x[["6"]], x[["7"]], x[["8"]], x[["9"]], x[["10"]],
    x[["11"]], x[["12"]], x[["13"]], x[["14"]], x[["15"]],
    x[["16"]], x[["17"]], x[["18"]], x[["19"]], x[["20"]],
    x[["21"]], x[["22"]], x[["23"]], x[["24"]], x[["25"]],
    x[["26"]], x[["27"]], x[["28"]], x[["29"]], x[["30"]],
    x[["31"]], x[["32"]], x[["33"]], x[["34"]], x[["35"]],
    x[["36"]], x[["37"]], x[["38"]]
)
y <- t(y)
dataset3 <- dataset %>%
    filter(NrmzMeanConfAll != "NA") %>%
    group_by(PPno) %>%
    summarise_at(vars(NrmzMeanConfPair, NrmzMeanConfEvent, NrmzMeanConfDetail, NrmzMeanConfAll), list(name = mean))
dataset3 <- cbind(dataset3, y)

dataset3$sumF <- dataset3$beF + dataset3$bpF
dataset3$sumR <- dataset3$beR + dataset3$bpR + dataset3$weR
dataset3$sumFR <- dataset3$sumF + dataset3$sumR
View(dataset3)

# ANOVAS
anova_all_F <- aov(NrmzMeanConfAll_name ~ sumF, data = dataset3)
summary(anova_all_F)
anova_all_R <- aov(NrmzMeanConfAll_name ~ sumR, data = dataset3)
summary(anova_all_R)
anova_all_FR <- aov(NrmzMeanConfAll_name ~ sumFR, data = dataset3)
summary(anova_all_FR)

anova_pair_F <- aov(NrmzMeanConfPair_name ~ sumF, data = dataset3)
summary(anova_pair_F)
anova_pair_R <- aov(NrmzMeanConfPair_name ~ sumR, data = dataset3)
summary(anova_pair_R)
anova_pair_FR <- aov(NrmzMeanConfPair_name ~ sumFR, data = dataset3)
summary(anova_pair_FR)

anova_event_F <- aov(NrmzMeanConfEvent_name ~ sumF, data = dataset3)
summary(anova_event_F)
anova_event_R <- aov(NrmzMeanConfEvent_name ~ sumR, data = dataset3)
summary(anova_event_R)
anova_event_FR <- aov(NrmzMeanConfEvent_name ~ sumFR, data = dataset3)
summary(anova_event_FR)

anova_detail_F <- aov(NrmzMeanConfDetail_name ~ sumF, data = dataset3)
summary(anova_detail_F)
anova_detail_R <- aov(NrmzMeanConfDetail_name ~ sumR, data = dataset3)
summary(anova_detail_R)
anova_detail_FR <- aov(NrmzMeanConfDetail_name ~ sumFR, data = dataset3)
summary(anova_detail_FR)

# AVERAGE FIXATION DURATION AND SACCADE AMPLITUDES
dataset$duration <- as.numeric(dataset$duration)
dataset$sac_amplitude <- as.numeric(dataset$sac_amplitude)
dataset$duration2 <- (dataset$duration) * (1000 / 256)
dataset4 <- dataset %>%
    filter(Refi != "[]")
View(dataset4)

tapply(dataset4$duration2, dataset4$Refi, summary, simplify = T)
tapply(dataset4$sac_amplitude, dataset4$Refi, summary, simplify = T)

anova_dur <- aov(duration2 ~ Refi, data = dataset4)
summary(anova_dur)
anova_sac <- aov(sac_amplitude ~ Refi, data = dataset4)
summary(anova_sac)

tukey_dur <- TukeyHSD(anova_dur)
tukey_dur
tukey_sac <- TukeyHSD(anova_sac)
tukey_sac

lm_dur <- lm(duration2 ~ Refi, data = dataset4)
summary(lm_dur)
lm_sac <- lm(sac_amplitude ~ Refi, data = dataset4)
summary(lm_sac)
