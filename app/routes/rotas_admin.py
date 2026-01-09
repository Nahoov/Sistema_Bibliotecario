from flask import Blueprint, request, redirect, url_for, render_template, flash, current_app

rotas_bp_admin= Blueprint('rotas_admin', __name__, url_prefix='/')