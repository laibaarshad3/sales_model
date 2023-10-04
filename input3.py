import argparse 

parser = argparse.ArgumentParser()

# store_nbr	family	onpromotion	dcoilwtico	city	type	cluster	year	month	day	holi_type	locale	locale_name	transferred
parser.add_argument("store_nbr" , type=int)
parser.add_argument("family" , type=str)
parser.add_argument("onpromotion" , type=int)
parser.add_argument("dcoilwtico" , type=int)
parser.add_argument("city" , type=str)
parser.add_argument("type" , type=str)
parser.add_argument("cluster" , type=int)
parser.add_argument("year" , type=int)
parser.add_argument("month" , type=int)
parser.add_argument("day" , type=int)
parser.add_argument("holi_type" , type=str)
parser.add_argument("locale" , type=str)
parser.add_argument("locale_name" , type=str)
parser.add_argument("transferred" , type=bool)
args = parser.parse_args()

args = parser.parse_args()
list = [list] 

list.append(args.store_nbr)
list.append(args.family)
list.append(args.onpromotion)
list.append(args.dcoilwtico)
list.append(args.city)
list.append(args.type)
list.append(args.cluster)
list.append(args.year)
list.append(args.month)
list.append(args.day)
list.append(args.holi_type)
list.append(args.locale)
list.append(args.locale_name)


if args.transferred == False:
    list.append(0)
elif args.transferred == True:
    list.append(1)


list = [list]
import joblib
load_e = joblib.load('encoder.pkl')
import pandas as pd
x_p=pd.DataFrame(list,columns=(["date","store_nbr","family","onpromotion","dcoilwtico","city","type","cluster","year","month","day","holi_type","locale","locale_name","transferred"]))
x_p_t= load_e.transform(x_p)
x_p_t=pd.DataFrame(x_p_t)

model = joblib.load("model.pkl")
pred = model.predict(x_p_t)


if not x_p_t.empty:
    print("Predicted Sales:", pred)
else:
    print("No data found for the specified criteria.")
