from selenium.webdriver.common.by import By
import time

class FeedbackHubHistoryPage:
    feedbackhub_id_input=(By.XPATH,"//app-record-manager-grid/div/ag-grid-angular/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/app-text-floating-filter/input")
    def feedback_id_aggrid(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*FeedbackHubHistoryPage.feedbackhub_id_input)
    
    feedbackhub_created_on_input=(By.XPATH,"//ag-grid-angular/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/input")
    def feedbackhub_createdon_aggrid(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(*FeedbackHubHistoryPage.feedbackhub_created_on_input)

    feedbackhub_leader_id_input=(By.XPATH,"//ag-grid-angular/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[3]/div[1]/app-text-floating-filter/input")
    def feedbackhub_leader_id_agrid(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*FeedbackHubHistoryPage.feedbackhub_leader_id_input)
    
    feedbackhub_pagename_input=(By.XPATH,"//ag-grid-angular/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[3]/div[1]/app-text-floating-filter/input")
    def feedbackhub_pagename_aggrid(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*FeedbackHubHistoryPage.feedbackhub_pagename_input)
    
    feedbackhub_dceo_rating_input=(By.XPATH,"//ag-grid-angular/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/app-text-floating-filter/input")
    def feedbackhub_dceo_rating_aggrid(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*FeedbackHubHistoryPage.feedbackhub_dceo_rating_input)
    
    feedbackhub_feature_rating_input=(By.XPATH,"//ag-grid-angular/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[1]/app-text-floating-filter/input")
    def feedbackhub_feature_rating_aggrid(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*FeedbackHubHistoryPage.feedbackhub_feature_rating_input)
    
    feedbackhub_feedback_input=(By.XPATH,"//ag-grid-angular/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[3]/div[1]/app-text-floating-filter/input")
    def feedbackhub_feedback_aggrid(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*FeedbackHubHistoryPage.feedbackhub_feedback_aggrid)
    
    feedbackhub_updatedon_input=(By.XPATH,"//ag-grid-angular/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[5]/div[1]/div/div[2]/div/div/div[2]/input")
    def feedbackhub_updatedon_aggrid(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*FeedbackHubHistoryPage.feedbackhub_updatedon_input)
    
    feedbackhub_status_input=(By.XPATH,"//ag-grid-angular/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[6]/div[1]/app-text-floating-filter/input")
    def feedbackhub_status_aggrid(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*FeedbackHubHistoryPage.feedbackhub_status_input)
    
    feedbackhub_comments_input=(By.XPATH,"//ag-grid-angular/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[7]/div[1]/app-text-floating-filter/input")
    def feedbackhub_comments_aggrid(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*FeedbackHubHistoryPage.feedbackhub_comments_input)
    
    feedbackhub_feedback_id_firstrow=(By.XPATH,"//ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[1]/div/span")
    def feedbackhub_feedback_id_firstrow_aggrid(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*FeedbackHubHistoryPage.feedbackhub_feedback_id_firstrow)

    feedbackhub_createdon_firstrow=(By.XPATH,"//ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[2]/div/span")
    def feedbackhub_createdon_firstrow_aggrid(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*FeedbackHubHistoryPage.feedbackhub_createdon_firstrow)
    
    feedbackhub_leaderid_firstrow=(By.XPATH,"//ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[3]/div/span")
    def feedbackhub_leaderid_firstrow_aggrid(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*FeedbackHubHistoryPage.feedbackhub_leaderid_firstrow)
    
    feedbackhub_leadername_firstrow="//ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[4]/div/span"
    def feedbackhub_leadername_firstrow_aggrid(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*FeedbackHubHistoryPage.feedbackhub_leadername_firstrow)
    
    feedbackhub_pagename_firstrow=(By.XPATH,"//ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[5]/div/span")
    def feedbackhub_pagename_firstrow_aggrid(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*FeedbackHubHistoryPage.feedbackhub_pagename_firstrow)

    feedbackhub_dceo_rating_firstrow=(By.XPATH,"//ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[7]/div/span")
    def feedbackhub_dceo_rating_firstrow_aggrid(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*FeedbackHubHistoryPage.feedbackhub_dceo_rating_firstrow)
    
    feedbackhub_feature_rating_firstrow=(By.XPATH,"//ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[3]/div/span")
    def feedbackhub_feature_rating_firstrow_aggrid(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*FeedbackHubHistoryPage.feedbackhub_feature_rating_firstrow)
    
    feedbackhub_updatedon_firstrow=(By.XPATH,"//ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[5]/div/span")
    def feedbackhub_updatedon_firstrow_aggrid(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*FeedbackHubHistoryPage.feedbackhub_updatedon_firstrow)
    
    feedbackhub_status_firstrow=(By.XPATH,"//ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[6]/div/span")
    def feedbackhub_status_firstrow_aggrid(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*FeedbackHubHistoryPage.feedbackhub_status_firstrow)
    
    feedbackhub_comments_firstrow=(By.XPATH,"//ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[7]/div/span")
    def feedbackhub_comments_firstrow_aggrid(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*FeedbackHubHistoryPage.feedbackhub_comments_firstrow)
    
    feedbackhub_edit_button_firstrow=(By.XPATH,"/html/body/app-root/div/div/app-feed-back-hub-admin/app-container/div/div[3]/div/app-record-manager-grid/div/ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[2]/div/span/app-feed-back-hub-admin-edit-cell-renderer/app-action-button/button")
    def feedbackhub_edit_button_firstrow_aggrid(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*FeedbackHubHistoryPage.feedbackhub_edit_button_firstrow)
    