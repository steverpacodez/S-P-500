   data = df_corr.values #gets the inner values/data of the df, not the index or headers
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)


heatmap=ax.pcolor(data,cmap=plt.cm.RdYlGn)
    fig.colorbar(heatmap) #creates pur legend
    ax.set_xticks(np.arrange(data.shape[0])+ 0.5, minor=False) #setting ticks to mark where the companies are lined up at every 0.5 mark
    ax.set_yticks(np.arrange(data.shape[1])+ 0.5, minor=False)
    ax.invert_yaxis #matplotlib graphs always have a small gap on top which makes sense but not in this case so it removes it
    ax.xaxis.tick_top() #moves the x-axis ticks that are normally at the bottom of the chart to the top because this is meant to be more of a table

    column_labels= df_corr.columns 
    row_labels= df_corr.index #column and labels should be identical in this case

    ax.set_xticklabels(column_labels)
    ax.set_ytiklabels(row_labels)
    plt.xticks(rotation=90)
    heatmap.set_clim(-1,1) #Sets a limit for the color scale
    plt.tight_layout()  #cleans things up on a messy graph
    plt.show()
