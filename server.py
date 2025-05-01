""" Flask app """

import json
import datetime
from flask import Flask, render_template, request, redirect, flash, url_for


def create_app(config=None, competitions=None, clubs=None):
    """ Function to create a Flask app"""

    def loadClubs():
        """ Function loads all clubs from json file """

        with open('clubs.json') as c:
            listOfClubs = json.load(c)['clubs']
            return listOfClubs

    def loadCompetitions():
        """ Function loads all comepetitions from json file """

        with open('competitions.json') as comps:
            listOfCompetitions = json.load(comps)['competitions']
            return listOfCompetitions

    app = Flask(__name__)
    if config:
        app.config.from_object(config)
    app.secret_key = 'something_special'

    competitions = competitions if competitions is not None else loadCompetitions()
    clubs = clubs if clubs is not None else loadClubs()

    @app.route('/')
    def index():
        return render_template('index.html', clubs=clubs)

    @app.route('/showSummary', methods=['POST'])
    def showSummary():
        """ Function displays summary page after successful login"""

        try:
            club = [club for club in clubs if club['email'] == request.form['email']][0]
            return render_template('welcome.html', club=club, competitions=competitions)
        except IndexError:
            return "Oops Sorry! The email was not found.", 404

    @app.route('/book/<competition>/<club>')
    def book(competition, club):
        """ Function redirects to page for booking places for competitions """

        foundClub = [c for c in clubs if c['name'] == club][0]
        foundCompetition = [c for c in competitions if c['name'] == competition][0]

        if foundClub and foundCompetition:
            # Checke the date when competition held
            competition_date = datetime.datetime.strptime(foundCompetition['date'][:10], "%Y-%m-%d")
            if competition_date.date() > datetime.date.today():
                return render_template('booking.html', club=foundClub, competition=foundCompetition)

            return f"""You cannot book places for the past competitions. This Competition held on
             {str(datetime.datetime.strptime(foundCompetition['date'][:10],'%Y-%m-%d'))}.""", 400

        else:
            flash("Something went wrong-please try again")
            return render_template('welcome.html', club=club, competitions=competitions)

    @app.route('/purchasePlaces', methods=['POST'])
    def purchasePlaces():
        """ Function to purchase places in a competition"""

        competition = [c for c in competitions if c['name'] == request.form['competition']][0]
        club = [c for c in clubs if c['name'] == request.form['club']][0]
        placesRequired = int(request.form['places'])

        # Check if club purchase more than 12 places per competition
        if placesRequired > 12:
            return "You cannot book more than 12 places per competition", 400
        
        # Check if club purchase places more than the available points
        if int(club['points']) < placesRequired:
            return f"You do not have enough points left to book the place. Points available:{club['points']}", 400
    
        # Deduct booked places from the club points
        club['points'] = int(club['points']) - placesRequired

        competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - placesRequired
        flash('Great-booking complete!')
        return render_template('welcome.html', club=club, competitions=competitions)

    @app.route('/logout')
    def logout():
        """ function to logout"""

        return redirect(url_for('index'))

    return app
