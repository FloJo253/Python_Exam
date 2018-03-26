# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..log_reg.models import User
from django.db import models
from datetime import datetime

class Quote(models.Model):
    quoted_by = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    creator = models.ForeignKey(User, related_name='created_by')
    favorite = models.ManyToManyField(User, related_name='faved_by')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    
    def __str__(self):
	    return 'quoted_by: {}, message {}, creator{}'.format(self.quoted_by, self.message, self.creator)
