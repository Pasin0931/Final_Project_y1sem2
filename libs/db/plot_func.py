import os
import sqlite3
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

connection_ = create_engine("sqlite:///histories.db")

class Plotter:
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, 'histories.db')
        self.connection_ = create_engine(f"sqlite:///{db_path}")

        self.in_game_ts_df = pd.read_sql_table('in_game_ts', con=self.connection_)
        self.player_statistic_df = pd.read_sql_table('player_statistic', con=self.connection_)
        self.point_usage_df = pd.read_sql_table('point_usage_statistic', con=self.connection_)
        self.species_defeated_df = pd.read_sql_table('species_defeated', con=self.connection_)

        plots_dir = os.path.join(BASE_DIR, 'plots')
        os.makedirs(plots_dir, exist_ok=True)

        self.plt_adr = [
            os.path.join(plots_dir, 'barplot.png'),
            os.path.join(plots_dir, 'pieplot.png'),
            os.path.join(plots_dir, 'lineplot.png'),
            os.path.join(plots_dir, 'tableplot.png')
        ]

        self.get_bar_plot()
        self.get_pie_plot()
        self.get_lines_plot()
        self.get_table_plot()

    def get_bar_plot(self):
        this_lab = []
        values_ = []
        for i in self.species_defeated_df:
            if i in ['id']:
                continue
            this_lab.append(i)
            values_.append(self.species_defeated_df[i].sum())
        tmp_df = pd.DataFrame({'Enemy type': this_lab, 'values': values_})
        ax = tmp_df.plot.bar(x="Enemy type", y="values", rot=0, title='Enemy Defeated', fontsize=8)
        ax.set_xlabel('Enemy Type', fontsize=10)
        ax.set_ylabel('Count', fontsize=10)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=20)
        ax.minorticks_on()

        ax.text(0.98, 0.85, f'Enemy killed: {sum(values_)}', transform=ax.transAxes, ha='right', va='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.5))
        plt.savefig(self.plt_adr[0], dpi=600, bbox_inches='tight')

    def get_pie_plot(self):
        plt.figure()
        this_lab = []
        values_ = []
        for i in self.point_usage_df:
            if i == 'id':
                continue
            this_lab.append(i)
            values_.append(self.point_usage_df[i].sum())
        tmp_df = pd.DataFrame({'Skills': this_lab, 'values': values_})
        plt.pie(values_, labels=this_lab, autopct='%1.1f%%')
        plt.title('Player choice of upgrade')
        # plt.show()
        plt.savefig(self.plt_adr[1], dpi=600, bbox_inches='tight')
        plt.clf()

    def get_lines_plot(self):
        plt.figure()
        x = np.arange(len(self.in_game_ts_df))

        width = 0.35
        plt.plot(x - width/2, self.in_game_ts_df['health'], label='Health')
        plt.plot(x + width/2, self.in_game_ts_df['points'], label='Points')

        # in_game_ts_df

        plt.xticks(x[::5], self.in_game_ts_df['time_stamp'][::5])

        plt.xticks(fontsize=7, rotation=45)
        plt.xlabel('Time (seconds)')
        plt.ylabel('Amount')

        zero_points = self.in_game_ts_df[self.in_game_ts_df['time_stamp'] == 0]
        # print(zero_points)

        game = 1
        for ts in zero_points['id']-1:
            # print(ts)
            plt.axvline(x=ts, color='red', linestyle='--')
            plt.text(ts+0.25, plt.ylim()[1]-45, f'game {game}', color='red', fontsize=10, rotation=270)
            game+=1
        game = 0

        plt.title('Player In-Game health x points received')
        plt.legend()
        # plt.show()
        plt.savefig(self.plt_adr[2], dpi=600, bbox_inches='tight')
        plt.clf()

    def get_table_plot(self):
        plt.figure()
        plt.axis('off')
        
        stats = self.in_game_ts_df[['health', 'points', 'time_stamp']].agg(['mean', 'median', 'std']).round(2)
        stats.columns = ['Health', 'Points', 'Time (seconds)']
        stats.index = ['Mean', 'Median', 'Stdev']
        
        table = plt.table(
            cellText=stats.values,
            rowLabels=stats.index,
            colLabels=stats.columns,
            loc='center',
            cellLoc='center'
        )
        table.auto_set_font_size(False)
        table.set_fontsize(12)
        table.scale(1.5, 2)
        plt.title('Player In-Game Statistics', fontsize=14, pad=20)
        plt.savefig(self.plt_adr[3], dpi=600, bbox_inches='tight')
        plt.clf()

    def get_plots_address(self):
        return self.plt_adr
    
# a = Plotter()
# b = a.get_plots_address
# print(b)