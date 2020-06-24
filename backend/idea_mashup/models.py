from django.db import models


class Who(models.Model):
    data = models.CharField(max_length=255)

    def __str__(self):
        return self.data


class What(models.Model):
    data = models.CharField(max_length=255)

    def __str__(self):
        return self.data


class Where(models.Model):
    data = models.CharField(max_length=255)

    def __str__(self):
        return self.data


class Why(models.Model):
    data = models.CharField(max_length=255)

    def __str__(self):
        return self.data
