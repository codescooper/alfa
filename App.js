import React from 'react';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Button, TouchableOpacity } from 'react-native';
import * as Speech from 'expo-speech';

export default function App() {
  const alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];

  const speak = (letter) => {
    const thingToSay = letter;
    Speech.speak(thingToSay);
  };

  const read = (letter) => {
    speak(letter);
  };

  const createRows = (array, elementsPerRow) => {
    const rows = [];
    let row = [];

    for (let i = 0; i < array.length; i++) {
      if (i > 0 && i % elementsPerRow === 0) {
        rows.push(row);
        row = [];
      }
      row.push(array[i]);
    }

    if (row.length > 0) {
      rows.push(row);
    }

    return rows;
  };

  const alphabetRows = createRows(alphabet, 5);

  return (
    <View style={styles.container}>
      <center><Text>Appuie sur une lettre pour entendre comment elle se prononce</Text></center>
      <StatusBar style="auto" />
      <View style={styles.grid}>
        {alphabetRows.map((row, rowIndex) => (
          <View key={rowIndex} style={styles.row}>
            {row.map((letter) => (
              <TouchableOpacity key={letter} style={styles.box} onPress={() => read(letter)}>
                <Text style={styles.letter}>{letter}</Text>
              </TouchableOpacity>
            ))}
          </View>
        ))}
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  grid: {
    marginTop: 20,
  },
  row: {
    flexDirection: 'row',
  },
  box: {
    width: 50,
    height: 50,
    backgroundColor: 'lightgray',
    margin: 10,
    alignItems: 'center',
    justifyContent: 'center',
  },
  letter: {
    fontSize: 20,
  },
});
