import React, {PureComponent} from 'react';
import DatePicker from "react-datepicker";

const defaultContainer = ({children}) => <div className="control-panel">{children}</div>;

export default class ControlPanel extends PureComponent {

  render() {
    const {handleChange, startTime, endTime, onChangeDay, allDay, onChangeAllDay, selectedTime} = this.props;
    const day = 24*60*60*1000;
    const days = Math.round((endTime - startTime) / day);

    //New lign added
    const startDate = new Date();

    const _handleChange = evt => {
      const daysChoose = evt.target.value;
      handleChange(daysChoose);
    }
    // End new ligne added



    const _onChangeDay = evt => {
      const daysToAdd = evt.target.value;
      // add selected days to start time to calculate new time
      const newTime = startTime + (daysToAdd * day);
      onChangeDay(newTime);
    }

    

    const formatTime = time => {
      const date = new Date(time);
      return `${date.getMonth() + 1}/${date.getDate()}/${date.getFullYear()}`
    }

    const Container = this.props.containerComponent || defaultContainer;

    return (
      <Container>
        <h3>FLOODMAP</h3>
        <p>Map showing the upcoming flood
          {/* <br />
          from <b>{formatTime(startTime)}</b> to <b>{formatTime(endTime)}</b>. */}
        </p>
        <hr />
        <div className="input">
          <label>All Passed Days</label>
          <input type="checkbox"
            name="allday"
            checked={allDay}
            onChange={evt => onChangeAllDay(evt.target.checked)}
            />
        </div>
        <div className={`input ${allDay ? 'disabled' : ''}`}>
          <label>Each Day: {formatTime(selectedTime)}</label>
          <input
            type="range"
            disabled={allDay}
            min={1}
            max={days}
            step={1}
            onChange={_onChangeDay}
            />
        </div>
        <div className="form-group">
          <DatePicker selected={startDate} onChange={_handleChange} />
        </div>
        {/* < hr />
        <p>Data source: <a href="https://docs.mapbox.com/mapbox-gl-js/assets/earthquakes.geojson">earthquakes.geojson</a></p>
        <div className="source-link">
          <a href="https://github.com/uber/react-map-gl/tree/4.0-release/examples/heatmap" target="_new">View Code ↗</a>
        </div> */}
      </Container>
    );
  }
}
