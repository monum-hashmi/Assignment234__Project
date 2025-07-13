# Python
from django.urls import path
from .views import (
    LanguageListView, LanguageCreateView, LanguageUpdateView, LanguageDeleteView, LanguageDetailView,
    TechnicalSkillListView, TechnicalSkillCreateView, TechnicalSkillUpdateView, TechnicalSkillDeleteView, TechnicalSkillDetailView,
    TemplateSelectorView, ClassicResumePreviewView, ModernResumePreviewView, CreativeResumePreviewView, TechnicalResumePreviewView, MinimalResumePreviewView
)

urlpatterns = [
    # Technical Skill URLs
    path('technical-skill/<int:pk>/edit/', TechnicalSkillUpdateView.as_view(), name='technical_skill_update'),
    path('technical-skill/<int:pk>/delete/', TechnicalSkillDeleteView.as_view(), name='technical_skill_delete'),
    path('technical-skill/<int:pk>/', TechnicalSkillDetailView.as_view(), name='technical_skill_detail'),
    path('technical-skill/', TechnicalSkillListView.as_view(), name='technical_skill_list'),
    path('technical-skill/add/', TechnicalSkillCreateView.as_view(), name='technical_skill_add'),

    # Language URLs
    path('language/<int:pk>/edit/', LanguageUpdateView.as_view(), name='language_update'),
    path('language/<int:pk>/delete/', LanguageDeleteView.as_view(), name='language_delete'),
    path('language/<int:pk>/', LanguageDetailView.as_view(), name='language_detail'),
    path('language/', LanguageListView.as_view(), name='language_list'),
    path('language/add/', LanguageCreateView.as_view(), name='language_add'),

    # Resume Template Selector
    path('template-selector/', TemplateSelectorView.as_view(), name='template_selector'),

    # Resume Previews
    path('preview/classic/<int:resume_id>/', ClassicResumePreviewView.as_view(), name='resume_preview_classic'),
    path('preview/modern/<int:resume_id>/', ModernResumePreviewView.as_view(), name='resume_preview_modern'),
    path('preview/creative/<int:resume_id>/', CreativeResumePreviewView.as_view(), name='resume_preview_creative'),
    path('preview/technical/<int:resume_id>/', TechnicalResumePreviewView.as_view(), name='resume_preview_technical'),
    path('preview/minimal/<int:resume_id>/', MinimalResumePreviewView.as_view(), name='resume_preview_minimal'),
]