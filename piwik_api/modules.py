"""Client classes for each Piwik module."""

from .base import BaseModule, api_method

class API(BaseModule): #noqa
    @api_method
    def getPiwikVersion(self, **args): #noqa
        return args

    @api_method
    def getIpFromHeader(self, **args): #noqa
        return args

    @api_method
    def getSettings(self, **args): #noqa
        return args

    @api_method
    def getSegmentsMetadata(self, **args): #noqa
        return args

    @api_method
    def getMetadata(self, **args): #noqa
        return args

    @api_method
    def getReportMetadata(self, **args): #noqa
        return args

    @api_method
    def getProcessedReport(self, **args): #noqa
        return args

    @api_method
    def getReportPagesMetadata(self, **args): #noqa
        return args

    @api_method
    def getWidgetMetadata(self, **args): #noqa
        return args

    @api_method
    def get(self, **args): #noqa
        return args

    @api_method
    def getRowEvolution(self, **args): #noqa
        return args

    @api_method
    def getBulkRequest(self, **args): #noqa
        return args

    @api_method
    def isPluginActivated(self, **args): #noqa
        return args

    @api_method
    def getSuggestedValuesForSegment(self, **args): #noqa
        return args

    @api_method
    def getGlossaryReports(self, **args): #noqa
        return args

    @api_method
    def getGlossaryMetrics(self, **args): #noqa
        return args


class AbTesting(BaseModule): #noqa
    @api_method
    def getMetricsOverview(self, **args): #noqa
        return args

    @api_method
    def getMetricDetails(self, **args): #noqa
        return args

    @api_method
    def addExperiment(self, **args): #noqa
        return args

    @api_method
    def updateExperiment(self, **args): #noqa
        return args

    @api_method
    def startExperiment(self, **args): #noqa
        return args

    @api_method
    def finishExperiment(self, **args): #noqa
        return args

    @api_method
    def archiveExperiment(self, **args): #noqa
        return args

    @api_method
    def getJsIncludeTemplate(self, **args): #noqa
        return args

    @api_method
    def getJsExperimentTemplate(self, **args): #noqa
        return args

    @api_method
    def getAllExperiments(self, **args): #noqa
        return args

    @api_method
    def getActiveExperiments(self, **args): #noqa
        return args

    @api_method
    def getExperimentsByStatuses(self, **args): #noqa
        return args

    @api_method
    def getExperiment(self, **args): #noqa
        return args

    @api_method
    def deleteExperiment(self, **args): #noqa
        return args

    @api_method
    def getAvailableStatuses(self, **args): #noqa
        return args

    @api_method
    def getAvailableSuccessMetrics(self, **args): #noqa
        return args

    @api_method
    def getAvailableTargetAttributes(self, **args): #noqa
        return args


class Actions(BaseModule): #noqa
    @api_method
    def get(self, **args): #noqa
        return args

    @api_method
    def getPageUrls(self, **args): #noqa
        return args

    @api_method
    def getPageUrlsFollowingSiteSearch(self, **args): #noqa
        return args

    @api_method
    def getPageTitlesFollowingSiteSearch(self, **args): #noqa
        return args

    @api_method
    def getEntryPageUrls(self, **args): #noqa
        return args

    @api_method
    def getExitPageUrls(self, **args): #noqa
        return args

    @api_method
    def getPageUrl(self, **args): #noqa
        return args

    @api_method
    def getPageTitles(self, **args): #noqa
        return args

    @api_method
    def getEntryPageTitles(self, **args): #noqa
        return args

    @api_method
    def getExitPageTitles(self, **args): #noqa
        return args

    @api_method
    def getPageTitle(self, **args): #noqa
        return args

    @api_method
    def getDownloads(self, **args): #noqa
        return args

    @api_method
    def getDownload(self, **args): #noqa
        return args

    @api_method
    def getOutlinks(self, **args): #noqa
        return args

    @api_method
    def getOutlink(self, **args): #noqa
        return args

    @api_method
    def getSiteSearchKeywords(self, **args): #noqa
        return args

    @api_method
    def getSiteSearchNoResultKeywords(self, **args): #noqa
        return args

    @api_method
    def getSiteSearchCategories(self, **args): #noqa
        return args


class ActivityLog(BaseModule): #noqa
    @api_method
    def getEntries(self, **args): #noqa
        return args

    @api_method
    def getEntryCount(self, **args): #noqa
        return args


class Annotations(BaseModule): #noqa
    @api_method
    def add(self, **args): #noqa
        return args

    @api_method
    def save(self, **args): #noqa
        return args

    @api_method
    def delete(self, **args): #noqa
        return args

    @api_method
    def deleteAll(self, **args): #noqa
        return args

    @api_method
    def get(self, **args): #noqa
        return args

    @api_method
    def getAll(self, **args): #noqa
        return args

    @api_method
    def getAnnotationCountForDates(self, **args): #noqa
        return args


class Bandwidth(BaseModule): #noqa
    @api_method
    def get(self, **args): #noqa
        return args


class Contents(BaseModule): #noqa
    @api_method
    def getContentNames(self, **args): #noqa
        return args

    @api_method
    def getContentPieces(self, **args): #noqa
        return args


class CustomAlerts(BaseModule): #noqa
    @api_method
    def getAlert(self, **args): #noqa
        return args

    @api_method
    def getValuesForAlertInPast(self, **args): #noqa
        return args

    @api_method
    def getAlerts(self, **args): #noqa
        return args

    @api_method
    def addAlert(self, **args): #noqa
        return args

    @api_method
    def editAlert(self, **args): #noqa
        return args

    @api_method
    def deleteAlert(self, **args): #noqa
        return args

    @api_method
    def getTriggeredAlerts(self, **args): #noqa
        return args


class CustomDimensions(BaseModule): #noqa
    @api_method
    def getCustomDimension(self, **args): #noqa
        return args

    @api_method
    def configureNewCustomDimension(self, **args): #noqa
        return args

    @api_method
    def configureExistingCustomDimension(self, **args): #noqa
        return args

    @api_method
    def getConfiguredCustomDimensions(self, **args): #noqa
        return args

    @api_method
    def getAvailableScopes(self, **args): #noqa
        return args

    @api_method
    def getAvailableExtractionDimensions(self, **args): #noqa
        return args


class CustomPiwikJs(BaseModule): #noqa
    @api_method
    def doesIncludePluginTrackersAutomatically(self, **args): #noqa
        return args


class CustomVariables(BaseModule): #noqa
    @api_method
    def getCustomVariables(self, **args): #noqa
        return args

    @api_method
    def getCustomVariablesValuesFromNameId(self, **args): #noqa
        return args

    @api_method
    def getUsagesOfSlots(self, **args): #noqa
        return args


class Dashboard(BaseModule): #noqa
    @api_method
    def getDashboards(self, **args): #noqa
        return args


class DevicePlugins(BaseModule): #noqa
    @api_method
    def getPlugin(self, **args): #noqa
        return args


class DevicesDetection(BaseModule): #noqa
    @api_method
    def getType(self, **args): #noqa
        return args

    @api_method
    def getBrand(self, **args): #noqa
        return args

    @api_method
    def getModel(self, **args): #noqa
        return args

    @api_method
    def getOsFamilies(self, **args): #noqa
        return args

    @api_method
    def getOsVersions(self, **args): #noqa
        return args

    @api_method
    def getBrowsers(self, **args): #noqa
        return args

    @api_method
    def getBrowserVersions(self, **args): #noqa
        return args

    @api_method
    def getBrowserEngines(self, **args): #noqa
        return args


class Events(BaseModule): #noqa
    @api_method
    def getCategory(self, **args): #noqa
        return args

    @api_method
    def getAction(self, **args): #noqa
        return args

    @api_method
    def getName(self, **args): #noqa
        return args

    @api_method
    def getActionFromCategoryId(self, **args): #noqa
        return args

    @api_method
    def getNameFromCategoryId(self, **args): #noqa
        return args

    @api_method
    def getCategoryFromActionId(self, **args): #noqa
        return args

    @api_method
    def getNameFromActionId(self, **args): #noqa
        return args

    @api_method
    def getActionFromNameId(self, **args): #noqa
        return args

    @api_method
    def getCategoryFromNameId(self, **args): #noqa
        return args


class ExampleAPI(BaseModule): #noqa
    @api_method
    def getPiwikVersion(self, **args): #noqa
        return args

    @api_method
    def getAnswerToLife(self, **args): #noqa
        return args

    @api_method
    def getObject(self, **args): #noqa
        return args

    @api_method
    def getSum(self, **args): #noqa
        return args

    @api_method
    def getNull(self, **args): #noqa
        return args

    @api_method
    def getDescriptionArray(self, **args): #noqa
        return args

    @api_method
    def getCompetitionDatatable(self, **args): #noqa
        return args

    @api_method
    def getMoreInformationAnswerToLife(self, **args): #noqa
        return args

    @api_method
    def getMultiArray(self, **args): #noqa
        return args


class Feedback(BaseModule): #noqa
    @api_method
    def sendFeedbackForFeature(self, **args): #noqa
        return args


class FormAnalytics(BaseModule): #noqa
    @api_method
    def addForm(self, **args): #noqa
        return args

    @api_method
    def updateForm(self, **args): #noqa
        return args

    @api_method
    def getForm(self, **args): #noqa
        return args

    @api_method
    def getForms(self, **args): #noqa
        return args

    @api_method
    def getFormsByStatuses(self, **args): #noqa
        return args

    @api_method
    def deleteForm(self, **args): #noqa
        return args

    @api_method
    def archiveForm(self, **args): #noqa
        return args

    @api_method
    def get(self, **args): #noqa
        return args

    @api_method
    def getEntryFields(self, **args): #noqa
        return args

    @api_method
    def getDropOffFields(self, **args): #noqa
        return args

    @api_method
    def getPageUrls(self, **args): #noqa
        return args

    @api_method
    def getFieldTimings(self, **args): #noqa
        return args

    @api_method
    def getFieldSize(self, **args): #noqa
        return args

    @api_method
    def getUneededFields(self, **args): #noqa
        return args

    @api_method
    def getMostUsedFields(self, **args): #noqa
        return args

    @api_method
    def getFieldCorrections(self, **args): #noqa
        return args

    @api_method
    def updateFormFieldDisplayName(self, **args): #noqa
        return args

    @api_method
    def getCounters(self, **args): #noqa
        return args

    @api_method
    def getCurrentMostPopularForms(self, **args): #noqa
        return args

    @api_method
    def getAutoCreationSettings(self, **args): #noqa
        return args

    @api_method
    def getAvailableStatuses(self, **args): #noqa
        return args

    @api_method
    def getAvailableFormRules(self, **args): #noqa
        return args

    @api_method
    def getAvailablePageRules(self, **args): #noqa
        return args


class Funnels(BaseModule): #noqa
    @api_method
    def getMetrics(self, **args): #noqa
        return args

    @api_method
    def getFunnelFlow(self, **args): #noqa
        return args

    @api_method
    def getFunnelEntries(self, **args): #noqa
        return args

    @api_method
    def getFunnelExits(self, **args): #noqa
        return args

    @api_method
    def getGoalFunnel(self, **args): #noqa
        return args

    @api_method
    def deleteGoalFunnel(self, **args): #noqa
        return args

    @api_method
    def setGoalFunnel(self, **args): #noqa
        return args

    @api_method
    def getAvailablePatternMatches(self, **args): #noqa
        return args

    @api_method
    def testUrlMatchesSteps(self, **args): #noqa
        return args


class Goals(BaseModule): #noqa
    @api_method
    def getGoal(self, **args): #noqa
        return args

    @api_method
    def getGoals(self, **args): #noqa
        return args

    @api_method
    def addGoal(self, **args): #noqa
        return args

    @api_method
    def updateGoal(self, **args): #noqa
        return args

    @api_method
    def deleteGoal(self, **args): #noqa
        return args

    @api_method
    def getItemsSku(self, **args): #noqa
        return args

    @api_method
    def getItemsName(self, **args): #noqa
        return args

    @api_method
    def getItemsCategory(self, **args): #noqa
        return args

    @api_method
    def get(self, **args): #noqa
        return args

    @api_method
    def getDaysToConversion(self, **args): #noqa
        return args

    @api_method
    def getVisitsUntilConversion(self, **args): #noqa
        return args


class HeatmapSessionRecording(BaseModule): #noqa
    @api_method
    def addHeatmap(self, **args): #noqa
        return args

    @api_method
    def updateHeatmap(self, **args): #noqa
        return args

    @api_method
    def addSessionRecording(self, **args): #noqa
        return args

    @api_method
    def updateSessionRecording(self, **args): #noqa
        return args

    @api_method
    def getHeatmap(self, **args): #noqa
        return args

    @api_method
    def getSessionRecording(self, **args): #noqa
        return args

    @api_method
    def deleteHeatmap(self, **args): #noqa
        return args

    @api_method
    def endHeatmap(self, **args): #noqa
        return args

    @api_method
    def deleteSessionRecording(self, **args): #noqa
        return args

    @api_method
    def endSessionRecording(self, **args): #noqa
        return args

    @api_method
    def getHeatmaps(self, **args): #noqa
        return args

    @api_method
    def getSessionRecordings(self, **args): #noqa
        return args

    @api_method
    def getRecordedSessions(self, **args): #noqa
        return args

    @api_method
    def getRecordedSession(self, **args): #noqa
        return args

    @api_method
    def deleteRecordedSession(self, **args): #noqa
        return args

    @api_method
    def deleteRecordedPageview(self, **args): #noqa
        return args

    @api_method
    def getRecordedHeatmapMetadata(self, **args): #noqa
        return args

    @api_method
    def getRecordedHeatmap(self, **args): #noqa
        return args

    @api_method
    def testUrlMatchPages(self, **args): #noqa
        return args

    @api_method
    def getAvailableStatuses(self, **args): #noqa
        return args

    @api_method
    def getAvailableTargetPageRules(self, **args): #noqa
        return args

    @api_method
    def getAvailableDeviceTypes(self, **args): #noqa
        return args

    @api_method
    def getAvailableHeatmapTypes(self, **args): #noqa
        return args

    @api_method
    def getEventTypes(self, **args): #noqa
        return args


class ImageGraph(BaseModule): #noqa
    @api_method
    def get(self, **args): #noqa
        return args


class Insights(BaseModule): #noqa
    @api_method
    def canGenerateInsights(self, **args): #noqa
        return args

    @api_method
    def getInsightsOverview(self, **args): #noqa
        return args

    @api_method
    def getMoversAndShakersOverview(self, **args): #noqa
        return args

    @api_method
    def getMoversAndShakers(self, **args): #noqa
        return args

    @api_method
    def getInsights(self, **args): #noqa
        return args


class LanguagesManager(BaseModule): #noqa
    @api_method
    def isLanguageAvailable(self, **args): #noqa
        return args

    @api_method
    def getAvailableLanguages(self, **args): #noqa
        return args

    @api_method
    def getAvailableLanguagesInfo(self, **args): #noqa
        return args

    @api_method
    def getAvailableLanguageNames(self, **args): #noqa
        return args

    @api_method
    def getTranslationsForLanguage(self, **args): #noqa
        return args

    @api_method
    def getLanguageForUser(self, **args): #noqa
        return args

    @api_method
    def setLanguageForUser(self, **args): #noqa
        return args

    @api_method
    def uses12HourClockForUser(self, **args): #noqa
        return args

    @api_method
    def set12HourClockForUser(self, **args): #noqa
        return args


class Live(BaseModule): #noqa
    @api_method
    def getCounters(self, **args): #noqa
        return args

    @api_method
    def getLastVisitsDetails(self, **args): #noqa
        return args

    @api_method
    def getVisitorProfile(self, **args): #noqa
        return args

    @api_method
    def getMostRecentVisitorId(self, **args): #noqa
        return args


class LogViewer(BaseModule): #noqa
    @api_method
    def getLogEntries(self, **args): #noqa
        return args

    @api_method
    def getAvailableLogReaders(self, **args): #noqa
        return args

    @api_method
    def getConfiguredLogReaders(self, **args): #noqa
        return args

    @api_method
    def getLogConfig(self, **args): #noqa
        return args


class LoginSaml(BaseModule): #noqa
    @api_method
    def saveSamlConfig(self, **args): #noqa
        return args

    @api_method
    def importIdPMetadata(self, **args): #noqa
        return args


class MarketingCampaignsReporting(BaseModule): #noqa
    @api_method
    def getName(self, **args): #noqa
        return args

    @api_method
    def getKeywordContentFromNameId(self, **args): #noqa
        return args

    @api_method
    def getKeyword(self, **args): #noqa
        return args

    @api_method
    def getSource(self, **args): #noqa
        return args

    @api_method
    def getMedium(self, **args): #noqa
        return args

    @api_method
    def getContent(self, **args): #noqa
        return args

    @api_method
    def getSourceMedium(self, **args): #noqa
        return args

    @api_method
    def getNameFromSourceMediumId(self, **args): #noqa
        return args


class Marketplace(BaseModule): #noqa
    @api_method
    def deleteLicenseKey(self, **args): #noqa
        return args

    @api_method
    def saveLicenseKey(self, **args): #noqa
        return args


class MediaAnalytics(BaseModule): #noqa
    @api_method
    def get(self, **args): #noqa
        return args

    @api_method
    def getCurrentNumPlays(self, **args): #noqa
        return args

    @api_method
    def getCurrentSumTimeSpent(self, **args): #noqa
        return args

    @api_method
    def getCurrentMostPlays(self, **args): #noqa
        return args

    @api_method
    def getVideoResources(self, **args): #noqa
        return args

    @api_method
    def getAudioResources(self, **args): #noqa
        return args

    @api_method
    def getVideoTitles(self, **args): #noqa
        return args

    @api_method
    def getAudioTitles(self, **args): #noqa
        return args

    @api_method
    def getGroupedVideoResources(self, **args): #noqa
        return args

    @api_method
    def getGroupedAudioResources(self, **args): #noqa
        return args

    @api_method
    def getVideoHours(self, **args): #noqa
        return args

    @api_method
    def getAudioHours(self, **args): #noqa
        return args

    @api_method
    def getVideoResolutions(self, **args): #noqa
        return args

    @api_method
    def getPlayers(self, **args): #noqa
        return args


class MobileMessaging(BaseModule): #noqa
    @api_method
    def areSMSAPICredentialProvided(self, **args): #noqa
        return args

    @api_method
    def getSMSProvider(self, **args): #noqa
        return args

    @api_method
    def setSMSAPICredential(self, **args): #noqa
        return args

    @api_method
    def addPhoneNumber(self, **args): #noqa
        return args

    @api_method
    def getCreditLeft(self, **args): #noqa
        return args

    @api_method
    def removePhoneNumber(self, **args): #noqa
        return args

    @api_method
    def validatePhoneNumber(self, **args): #noqa
        return args

    @api_method
    def deleteSMSAPICredential(self, **args): #noqa
        return args

    @api_method
    def setDelegatedManagement(self, **args): #noqa
        return args

    @api_method
    def getDelegatedManagement(self, **args): #noqa
        return args


class MultiSites(BaseModule): #noqa
    @api_method
    def getAll(self, **args): #noqa
        return args

    @api_method
    def getOne(self, **args): #noqa
        return args


class Overlay(BaseModule): #noqa
    @api_method
    def getTranslations(self, **args): #noqa
        return args

    @api_method
    def getExcludedQueryParameters(self, **args): #noqa
        return args

    @api_method
    def getFollowingPages(self, **args): #noqa
        return args


class Provider(BaseModule): #noqa
    @api_method
    def getProvider(self, **args): #noqa
        return args


class Referrers(BaseModule): #noqa
    @api_method
    def getReferrerType(self, **args): #noqa
        return args

    @api_method
    def getAll(self, **args): #noqa
        return args

    @api_method
    def getKeywords(self, **args): #noqa
        return args

    @api_method
    def getKeywordsForPageUrl(self, **args): #noqa
        return args

    @api_method
    def getKeywordsForPageTitle(self, **args): #noqa
        return args

    @api_method
    def getSearchEnginesFromKeywordId(self, **args): #noqa
        return args

    @api_method
    def getSearchEngines(self, **args): #noqa
        return args

    @api_method
    def getKeywordsFromSearchEngineId(self, **args): #noqa
        return args

    @api_method
    def getCampaigns(self, **args): #noqa
        return args

    @api_method
    def getKeywordsFromCampaignId(self, **args): #noqa
        return args

    @api_method
    def getWebsites(self, **args): #noqa
        return args

    @api_method
    def getUrlsFromWebsiteId(self, **args): #noqa
        return args

    @api_method
    def getSocials(self, **args): #noqa
        return args

    @api_method
    def getUrlsForSocial(self, **args): #noqa
        return args

    @api_method
    def getNumberOfDistinctSearchEngines(self, **args): #noqa
        return args

    @api_method
    def getNumberOfDistinctKeywords(self, **args): #noqa
        return args

    @api_method
    def getNumberOfDistinctCampaigns(self, **args): #noqa
        return args

    @api_method
    def getNumberOfDistinctWebsites(self, **args): #noqa
        return args

    @api_method
    def getNumberOfDistinctWebsitesUrls(self, **args): #noqa
        return args


class Resolution(BaseModule): #noqa
    @api_method
    def getResolution(self, **args): #noqa
        return args

    @api_method
    def getConfiguration(self, **args): #noqa
        return args


class RollUpReporting(BaseModule): #noqa
    @api_method
    def addRollUp(self, **args): #noqa
        return args

    @api_method
    def updateRollUp(self, **args): #noqa
        return args

    @api_method
    def getRollUps(self, **args): #noqa
        return args


class SEO(BaseModule): #noqa
    @api_method
    def getRank(self, **args): #noqa
        return args


class ScheduledReports(BaseModule): #noqa
    @api_method
    def addReport(self, **args): #noqa
        return args

    @api_method
    def updateReport(self, **args): #noqa
        return args

    @api_method
    def deleteReport(self, **args): #noqa
        return args

    @api_method
    def getReports(self, **args): #noqa
        return args

    @api_method
    def generateReport(self, **args): #noqa
        return args

    @api_method
    def sendReport(self, **args): #noqa
        return args


class SearchEngineKeywordsPerformance(BaseModule): #noqa
    @api_method
    def getKeywords(self, **args): #noqa
        return args

    @api_method
    def getKeywordsBing(self, **args): #noqa
        return args

    @api_method
    def getKeywordsGoogleWeb(self, **args): #noqa
        return args

    @api_method
    def getKeywordsGoogleImage(self, **args): #noqa
        return args

    @api_method
    def getKeywordsGoogleVideo(self, **args): #noqa
        return args

    @api_method
    def getCrawlingOverviewBing(self, **args): #noqa
        return args

    @api_method
    def getCrawlingErrorsGoogle(self, **args): #noqa
        return args

    @api_method
    def getCrawlingErrorsGoogleSmartphone(self, **args): #noqa
        return args

    @api_method
    def getCrawlingErrorsGoogleDesktop(self, **args): #noqa
        return args


class SegmentEditor(BaseModule): #noqa
    @api_method
    def isUserCanAddNewSegment(self, **args): #noqa
        return args

    @api_method
    def delete(self, **args): #noqa
        return args

    @api_method
    def update(self, **args): #noqa
        return args

    @api_method
    def add(self, **args): #noqa
        return args

    @api_method
    def get(self, **args): #noqa
        return args

    @api_method
    def getAll(self, **args): #noqa
        return args


class SitesManager(BaseModule): #noqa
    @api_method
    def getJavascriptTag(self, **args): #noqa
        return args

    @api_method
    def getImageTrackingCode(self, **args): #noqa
        return args

    @api_method
    def getSitesFromGroup(self, **args): #noqa
        return args

    @api_method
    def getSitesGroups(self, **args): #noqa
        return args

    @api_method
    def getSiteFromId(self, **args): #noqa
        return args

    @api_method
    def getSiteUrlsFromId(self, **args): #noqa
        return args

    @api_method
    def getAllSites(self, **args): #noqa
        return args

    @api_method
    def getAllSitesId(self, **args): #noqa
        return args

    @api_method
    def getSitesWithAdminAccess(self, **args): #noqa
        return args

    @api_method
    def getSitesWithViewAccess(self, **args): #noqa
        return args

    @api_method
    def getSitesWithAtLeastViewAccess(self, **args): #noqa
        return args

    @api_method
    def getSitesIdWithAdminAccess(self, **args): #noqa
        return args

    @api_method
    def getSitesIdWithViewAccess(self, **args): #noqa
        return args

    @api_method
    def getSitesIdWithAtLeastViewAccess(self, **args): #noqa
        return args

    @api_method
    def getSitesIdFromSiteUrl(self, **args): #noqa
        return args

    @api_method
    def addSite(self, **args): #noqa
        return args

    @api_method
    def getSiteSettings(self, **args): #noqa
        return args

    @api_method
    def deleteSite(self, **args): #noqa
        return args

    @api_method
    def addSiteAliasUrls(self, **args): #noqa
        return args

    @api_method
    def setSiteAliasUrls(self, **args): #noqa
        return args

    @api_method
    def getIpsForRange(self, **args): #noqa
        return args

    @api_method
    def setGlobalExcludedIps(self, **args): #noqa
        return args

    @api_method
    def setGlobalSearchParameters(self, **args): #noqa
        return args

    @api_method
    def getSearchKeywordParametersGlobal(self, **args): #noqa
        return args

    @api_method
    def getSearchCategoryParametersGlobal(self, **args): #noqa
        return args

    @api_method
    def getExcludedQueryParametersGlobal(self, **args): #noqa
        return args

    @api_method
    def getExcludedUserAgentsGlobal(self, **args): #noqa
        return args

    @api_method
    def setGlobalExcludedUserAgents(self, **args): #noqa
        return args

    @api_method
    def isSiteSpecificUserAgentExcludeEnabled(self, **args): #noqa
        return args

    @api_method
    def setSiteSpecificUserAgentExcludeEnabled(self, **args): #noqa
        return args

    @api_method
    def getKeepURLFragmentsGlobal(self, **args): #noqa
        return args

    @api_method
    def setKeepURLFragmentsGlobal(self, **args): #noqa
        return args

    @api_method
    def setGlobalExcludedQueryParameters(self, **args): #noqa
        return args

    @api_method
    def getExcludedIpsGlobal(self, **args): #noqa
        return args

    @api_method
    def getDefaultCurrency(self, **args): #noqa
        return args

    @api_method
    def setDefaultCurrency(self, **args): #noqa
        return args

    @api_method
    def getDefaultTimezone(self, **args): #noqa
        return args

    @api_method
    def setDefaultTimezone(self, **args): #noqa
        return args

    @api_method
    def updateSite(self, **args): #noqa
        return args

    @api_method
    def getCurrencyList(self, **args): #noqa
        return args

    @api_method
    def getCurrencySymbols(self, **args): #noqa
        return args

    @api_method
    def isTimezoneSupportEnabled(self, **args): #noqa
        return args

    @api_method
    def getTimezonesList(self, **args): #noqa
        return args

    @api_method
    def getUniqueSiteTimezones(self, **args): #noqa
        return args

    @api_method
    def renameGroup(self, **args): #noqa
        return args

    @api_method
    def getPatternMatchSites(self, **args): #noqa
        return args

    @api_method
    def getNumWebsitesToDisplayPerPage(self, **args): #noqa
        return args


class Transitions(BaseModule): #noqa
    @api_method
    def getTransitionsForPageTitle(self, **args): #noqa
        return args

    @api_method
    def getTransitionsForPageUrl(self, **args): #noqa
        return args

    @api_method
    def getTransitionsForAction(self, **args): #noqa
        return args

    @api_method
    def getTranslations(self, **args): #noqa
        return args


class TreemapVisualization(BaseModule): #noqa
    @api_method
    def getTreemapData(self, **args): #noqa
        return args


class UserCountry(BaseModule): #noqa
    @api_method
    def getCountry(self, **args): #noqa
        return args

    @api_method
    def getContinent(self, **args): #noqa
        return args

    @api_method
    def getRegion(self, **args): #noqa
        return args

    @api_method
    def getCity(self, **args): #noqa
        return args

    @api_method
    def getCountryCodeMapping(self, **args): #noqa
        return args

    @api_method
    def getLocationFromIP(self, **args): #noqa
        return args

    @api_method
    def setLocationProvider(self, **args): #noqa
        return args

    @api_method
    def getNumberOfDistinctCountries(self, **args): #noqa
        return args


class UserId(BaseModule): #noqa
    @api_method
    def getUsers(self, **args): #noqa
        return args


class UserLanguage(BaseModule): #noqa
    @api_method
    def getLanguage(self, **args): #noqa
        return args

    @api_method
    def getLanguageCode(self, **args): #noqa
        return args


class UsersFlow(BaseModule): #noqa
    @api_method
    def getUsersFlowPretty(self, **args): #noqa
        return args

    @api_method
    def getUsersFlow(self, **args): #noqa
        return args

    @api_method
    def getInteractionActions(self, **args): #noqa
        return args


class UsersManager(BaseModule): #noqa
    @api_method
    def setUserPreference(self, **args): #noqa
        return args

    @api_method
    def getUserPreference(self, **args): #noqa
        return args

    @api_method
    def getUsers(self, **args): #noqa
        return args

    @api_method
    def getUsersLogin(self, **args): #noqa
        return args

    @api_method
    def getUsersSitesFromAccess(self, **args): #noqa
        return args

    @api_method
    def getUsersAccessFromSite(self, **args): #noqa
        return args

    @api_method
    def getUsersWithSiteAccess(self, **args): #noqa
        return args

    @api_method
    def getSitesAccessFromUser(self, **args): #noqa
        return args

    @api_method
    def getUser(self, **args): #noqa
        return args

    @api_method
    def getUserByEmail(self, **args): #noqa
        return args

    @api_method
    def addUser(self, **args): #noqa
        return args

    @api_method
    def setSuperUserAccess(self, **args): #noqa
        return args

    @api_method
    def hasSuperUserAccess(self, **args): #noqa
        return args

    @api_method
    def getUsersHavingSuperUserAccess(self, **args): #noqa
        return args

    @api_method
    def regenerateTokenAuth(self, **args): #noqa
        return args

    @api_method
    def updateUser(self, **args): #noqa
        return args

    @api_method
    def deleteUser(self, **args): #noqa
        return args

    @api_method
    def userExists(self, **args): #noqa
        return args

    @api_method
    def userEmailExists(self, **args): #noqa
        return args

    @api_method
    def getUserLoginFromUserEmail(self, **args): #noqa
        return args

    @api_method
    def setUserAccess(self, **args): #noqa
        return args

    @api_method
    def createTokenAuth(self, **args): #noqa
        return args

    @api_method
    def getTokenAuth(self, **args): #noqa
        return args


class VisitFrequency(BaseModule): #noqa
    @api_method
    def get(self, **args): #noqa
        return args


class VisitTime(BaseModule): #noqa
    @api_method
    def getVisitInformationPerLocalTime(self, **args): #noqa
        return args

    @api_method
    def getVisitInformationPerServerTime(self, **args): #noqa
        return args

    @api_method
    def getByDayOfWeek(self, **args): #noqa
        return args


class VisitorInterest(BaseModule): #noqa
    @api_method
    def getNumberOfVisitsPerVisitDuration(self, **args): #noqa
        return args

    @api_method
    def getNumberOfVisitsPerPage(self, **args): #noqa
        return args

    @api_method
    def getNumberOfVisitsByDaysSinceLast(self, **args): #noqa
        return args

    @api_method
    def getNumberOfVisitsByVisitCount(self, **args): #noqa
        return args


class VisitsSummary(BaseModule): #noqa
    @api_method
    def get(self, **args): #noqa
        return args

    @api_method
    def getVisits(self, **args): #noqa
        return args

    @api_method
    def getUniqueVisitors(self, **args): #noqa
        return args

    @api_method
    def getUsers(self, **args): #noqa
        return args

    @api_method
    def getActions(self, **args): #noqa
        return args

    @api_method
    def getMaxActions(self, **args): #noqa
        return args

    @api_method
    def getBounceCount(self, **args): #noqa
        return args

    @api_method
    def getVisitsConverted(self, **args): #noqa
        return args

    @api_method
    def getSumVisitsLength(self, **args): #noqa
        return args

    @api_method
    def getSumVisitsLengthPretty(self, **args): #noqa
        return args
